
def handle_kwargs(args):
    subcommand = args.subcommand 


    kwargs = {}

    #if (subcommand == "mol2csv"): 
    kwargs = vars(args)
    return kwargs
