
def handle_kwargs(args):
    subcommand = args.subcommand 

    kwargs = {}
    kwargs = vars(args) 
    #if (subcommand == "execute"):
        #if kwargs['psql_script']:
        #    with open(str(kwargs["str_2_exe"]),'r') as readlines:
        #        print(readlines)
        #        lines = readlines.readlines()
        #        for line in lines:
        #            print(line)
        #            kwargs["str_2_exe"] 

    return kwargs
