#!/usr/bin/env python3
import json
import sys,os

DIRNAME=''
frozen = 'not'

#Since PyInstaller doesn't give you the PATH when you 
#print the base dir name, you have to 
#get the path of the executable and edit to get the dir you want
#if you want to check it out read the the documentation:
#https://pyinstaller.org/en/stable/runtime-information.html#run-time-information
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    #frozen = 'ever so'
    #bundle_dir = sys._MEIPASS
    DIRNAME=(os.path.dirname(os.path.dirname(sys.executable))+"/src/mol2db/config/")

#But if you are running in a regular python envrionemt (No Pyinstaller!)
#you can just get the dirname as shown below
else:
    # we are running in a normal Python environment
    DIRNAME = os.path.dirname(os.path.abspath(__file__)) + '/'

#$print( 'we are',frozen,'frozen')
#$print( 'bundle dir is', bundle_dir )
#$print( 'sys.argv[0] is', sys.argv[0] )
#$print( 'sys.executable is', sys.executable )
#$print( 'os.getcwd is', os.getcwd() )

def make_kwargs(args):

    kwargs = {}
    kwargs = vars(args) 

    return kwargs

def if_any_exist(**kwargs): 
    if  kwargs['dbname']    or \
        kwargs['user_name'] or \
        kwargs['pw']        or \
        kwargs['ht']        or \
        kwargs['prt']:
        return True
    else:
        return False


def source(**kwargs):

    config_f            = open(kwargs['what_to_source'])
    config_data         = json.load(config_f)

    with open(kwargs['what_to_source'], "w") as outfile:
        outfile.write(json.dumps(config_data, indent=4))

    #fill the kwargs keys with credential
    #information
    kwargs['dbname']    = config_data['database_name']
    kwargs['user_name'] = config_data['user_name']
    kwargs['pw']        = config_data['password']
    kwargs['ht']        = config_data['host']
    kwargs['prt']       = config_data['port']

    return kwargs

def make_your_own_kw(**kwargs):

    if if_any_exist(**kwargs):
        tmp_dict_config = dict()
        tmp_dict_config['database_name'] = kwargs['dbname']
        tmp_dict_config['user_name'] = kwargs['user_name']
        tmp_dict_config['password'] = kwargs['pw']
        tmp_dict_config['host'] = kwargs['ht']
        tmp_dict_config['port'] = kwargs['prt']


        if kwargs['subcommand'] == "createsource":
            #creating config file that contains your information. 
            with open(DIRNAME+kwargs['name_create'], "w") as outfile:
                outfile.write(json.dumps(tmp_dict_config, indent=4))
                print(kwargs['name_create']+ " created!")

        elif  kwargs['subcommand'] == "updatesource":
            #creating config file that contains your information. 
            with open(DIRNAME+kwargs['name_update'], "w") as outfile:
                outfile.write(json.dumps(tmp_dict_config, indent=4))
                print(kwargs['name_update']+ " updated!") 
    else:
        print("you have placed no input flags for configuration")


def set_configure (args):
    kwargs = {}
    kwargs = make_kwargs(args)

    #if there is source command but you want to input your own
    #this will automatically create a config file and output a json 
    #based on the input flags and where you place the path
    if kwargs['subcommand'] == "createsource" and kwargs['name_create']:
        if (os.path.exists(DIRNAME+kwargs['name_create'])):  
            sys.exit(kwargs['name_create'] + ' already exists. Name it something else. exiting...')
        make_your_own_kw(**kwargs)
   
    #removes the config file
    elif kwargs['subcommand'] == "deletesource" and kwargs['name_delete']:
        if not (os.path.exists(DIRNAME+kwargs['name_delete'])):
            sys.exit(kwargs['name_delete'] + " does not exists. Name it something else. exiting...")
        else:
            os.remove(DIRNAME+kwargs['name_delete'])
            print(kwargs['name_delete']+ ' deleted!')
        sys.exit()    

    #update the config file
    elif kwargs['subcommand'] == "updatesource":
        if os.path.exists(DIRNAME+kwargs['name_update']):
            make_your_own_kw(**kwargs)
        else:
            sys.exit(kwargs['name_update'] + " does not exist to update.")
        sys.exit()

    #if you are not sourcing AND there are no filled in inputs
    #for the credential information try to find the config file
    #and load the creds up. if not, exit 
    elif kwargs['cred']:
        if (if_any_exist(**kwargs)):
            print("remove any flags if sourcing. exiting...")
            sys.exit()

        try:
            config_f        = open(DIRNAME + kwargs['cred'])
        except FileNotFoundError:
            print("credential config file not found. Please source the file")
            sys.exit()
        except KeyError:
            print("you forgot to name config file")
            sys.exit()
    
        config_data         = json.load(config_f)
        kwargs['dbname']    = config_data['database_name']
        kwargs['user_name'] = config_data['user_name']
        kwargs['pw']        = config_data['password']
        kwargs['ht']        = config_data['host']
        kwargs['prt']       = config_data['port']
        return kwargs

    return kwargs
