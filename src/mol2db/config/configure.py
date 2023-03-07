import json
import sys,os

def make_kwargs(args):

    kwargs = {}
    kwargs = vars(args) 

    return kwargs


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

    if kwargs['dbname']         or \
            kwargs['user_name'] or \
            kwargs['pw']        or \
            kwargs['ht']        or \
            kwargs['prt']:
        tmp_dict_config = dict()
        tmp_dict_config['database_name'] = kwargs['dbname']
        tmp_dict_config['user_name'] = kwargs['user_name']
        tmp_dict_config['password'] = kwargs['pw']
        tmp_dict_config['host'] = kwargs['ht']
        tmp_dict_config['port'] = kwargs['prt']

        #creating config file that contains your information. 
        with open('./mol2db/config/'+kwargs['name_create'], "w") as outfile:
            outfile.write(json.dumps(tmp_dict_config, indent=4))
            print(kwargs['name_create']+ " created!")
    else:
        print("you have placed no input flags for configuration")
        sys.exit()


def set_configure (args):
    kwargs = {}
    kwargs = make_kwargs(args)

    #if there is source command but you want to input your own
    #this will automatically create a config file and output a json 
    #based on the input flags and where you place the path
    if kwargs['subcommand'] == "createsource" and kwargs['name_create']:
        if (os.path.exists('./mol2db/config/'+kwargs['name_create'])):  
            print(kwargs['name_create'] + ' already exists. Name it something else. exiting...')
            sys.exit()
        make_your_own_kw(**kwargs)
   
    #removes the config file
    elif kwargs['subcommand'] == "deletesource" and kwargs['name_delete']:
        if not (os.path.exists('./mol2db/config/'+kwargs['name_delete'])):
            print(kwargs['name_delete'] + " does not exists. Name it something else. exiting...") 
        else:
            os.remove('./mol2db/config/'+kwargs['name_delete'])
            print(kwargs['name_delete']+ ' deleted!')
 
        sys.exit()    
    #if you are not sourcing AND there are no filled in inputs
    #for the credential information try to find the config file
    #and load the creds up. if not, exit 
    elif kwargs['cred']:
        if (kwargs['dbname']    or \
            kwargs['user_name'] or \
            kwargs['pw']        or \
            kwargs['ht']        or \
            kwargs['prt']):

            print("remove any flags if sourcing. exiting...")
            sys.exit()

        try:
            config_f        = open('./mol2db/config/' + kwargs['cred'])
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
