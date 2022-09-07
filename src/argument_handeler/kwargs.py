
def handle_kwargs(args):
 

    if (args.job == "mol2csv"): 
        print("kwargs_mol2csv")
    elif (args.job == "str2exe"):
        kwargs = {"dbname":args.dbname,"user_name":args.user,"pw":args.pw,"ht":args.host,"prt":args.port} 

    return kwargs
