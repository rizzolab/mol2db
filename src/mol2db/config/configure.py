#!/usr/bin/env python3
import json
import sys, os
import getpass

# import others
from mol2db.config.hashing import get_hash


DIRNAME = ""
frozen = "not"
default_config = "mol2db.config"

# Since PyInstaller doesn't give you the PATH when you
# print the base dir name, you have to
# get the path of the executable and edit to get the dir you want
# if you want to check it out read the the documentation:
# https://pyinstaller.org/en/stable/runtime-information.html#run-time-information
if getattr(sys, "frozen", False):
    # we are running in a bundle
    # frozen = 'ever so'
    # bundle_dir = sys._MEIPASS
    DIRNAME = os.path.dirname(os.path.dirname(sys.executable))
    # DIRNAME = sys._MEIPASS

# But if you are running in a regular python envrionemt (No Pyinstaller!)
# you can just get the dirname as shown below
else:
    # we are running in a normal Python environment
    DIRNAME = os.path.dirname(os.path.abspath(__file__)) + "/"

# print( 'we are',frozen,'frozen')
# print( 'bundle dir is', bundle_dir )
# print( 'sys.argv[0] is', sys.argv[0] )
# print( 'sys.executable is', sys.executable )
# print( 'os.getcwd is', os.getcwd() )


def make_kwargs(args):
    kwargs = {}
    kwargs = vars(args)
    if all(v is None for v in [args.dbname, args.user_name, args.ht, args.prt]):
        return kwargs
    elif kwargs["subcommand"] in ["updatesource", "createsource"]:
        pw_dec = input("Do you want to add a password? (y/[n])")

        if pw_dec == "n" or pw_dec != "y":
            return kwargs

        PW = getpass.getpass()
        hashed_pw = get_hash(str(PW))
        kwargs["pw"] = hashed_pw

    return kwargs


def if_any_exist(**kwargs):
    if "pw" in kwargs:
        return True
    elif kwargs["dbname"] or kwargs["user_name"] or kwargs["ht"] or kwargs["prt"]:
        return True
    else:
        return False


def source(**kwargs):
    config_f = open(kwargs["cred"])
    config_data = json.load(config_f)

    with open(DIRNAME + "/" + kwargs["cred"], "w") as outfile:
        outfile.write(json.dumps(config_data, indent=4))

    # fill the kwargs keys with credential
    # information
    kwargs["dbname"] = config_data["database_name"]
    kwargs["user_name"] = config_data["user_name"]
    kwargs["pw"] = config_data["password"]
    kwargs["ht"] = config_data["host"]
    kwargs["prt"] = config_data["port"]

    return kwargs


def make_your_own_kw(**kwargs):
    str_cred = str(kwargs["cred"])

    if if_any_exist(**kwargs):
        hashed_pw = get_hash(str(kwargs.get("pw")))

        tmp_dict_config = dict()
        tmp_dict_config["database_name"] = kwargs["dbname"]
        tmp_dict_config["user_name"] = kwargs["user_name"]
        tmp_dict_config["password"] = hashed_pw
        tmp_dict_config["host"] = kwargs["ht"]
        tmp_dict_config["port"] = kwargs["prt"]

        if kwargs["subcommand"] == "createsource":
            # creating config file that contains your information.
            with open(DIRNAME + "/" + str_cred, "w") as outfile:
                outfile.write(json.dumps(tmp_dict_config, indent=4))
                print(str_cred + " created!")

        elif kwargs["subcommand"] == "updatesource":
            # creating config file that contains your information.
            with open(DIRNAME + "/" + str_cred, "w") as outfile:
                outfile.write(json.dumps(tmp_dict_config, indent=4))
                print(str_cred + " updated!")
    else:
        print("you have placed no input flags for configuration")


def set_configure(args):
    kwargs = {}
    kwargs = make_kwargs(args)

    if kwargs["cred"] == None:
        kwargs["cred"] = default_config

    str_cred = str(kwargs["cred"])

    # if there is source command but you want to input your own
    # this will automatically create a config file and output a json
    # based on the input flags and where you place the path
    if kwargs["subcommand"] == "createsource" and if_any_exist(**kwargs):
        if os.path.exists(DIRNAME + "/" + str_cred):
            sys.exit(str_cred + " already exists. Just update it exiting...")
        make_your_own_kw(**kwargs)

    # removes the config file
    elif kwargs["subcommand"] == "deletesource":
        if not (os.path.exists(DIRNAME + "/" + str_cred)):
            sys.exit(str_cred + " does not exists. exiting...")
        else:
            os.remove(DIRNAME + "/" + str_cred)
            print(str_cred + " deleted!")
        sys.exit()

    # update the config file
    elif kwargs["subcommand"] == "updatesource" and if_any_exist(**kwargs):
        if os.path.exists(DIRNAME + "/" + str_cred):
            make_your_own_kw(**kwargs)
        else:
            sys.exit(str_cred + " does not exist to update. please create one.")
        sys.exit()
    elif (
        kwargs["subcommand"] in ["updatesource", "createsource"]
        and if_any_exist(**kwargs) == False
    ):
        sys.exit("You need flags if you want to update or create credential file")

    # adding flags always takes precedance over no flag
    # or specified creds
    elif if_any_exist(**kwargs):
        return kwargs

    # if you are not sourcing AND there are no filled in inputs
    # for the credential information try to find the config file
    # and load the creds up. if not, exit
    elif (
        kwargs["subcommand"] != "updatesource"
        and kwargs["subcommand"] != "createsource"
    ):
        if if_any_exist(**kwargs):
            print("remove any flags if sourcing. exiting...")
            sys.exit()
        try:
            config_f = open(DIRNAME + "/" + str(str_cred))
        except FileNotFoundError:
            print("credential config file not found. Please source the file")
            sys.exit()
        except KeyError:
            print("you forgot to name config file")
            sys.exit()
        # else:
        #    try:
        #        config_f        = open(DIRNAME + default_config)
        #    except FileNotFoundError:
        #        print(f"credential config file {default_config} not found. Please source the file")
        #        sys.exit()
        #    except KeyError:
        #        print("you forgot to name config file")
        #        sys.exit()

        config_data = json.load(config_f)
        kwargs["dbname"] = config_data["database_name"]
        kwargs["user_name"] = config_data["user_name"]
        kwargs["ht"] = config_data["host"]
        kwargs["prt"] = config_data["port"]
        kwargs["pw"] = config_data["password"]
        return kwargs

    return kwargs
