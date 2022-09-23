
#import psycopg, which is a python psql interfacing program
import psycopg
from write import write_exe as wt

#def connect2psql (dbname="",user_name="",pw="",ht="",prt=""):
def connect2psql (**kwargs):

    conn = psycopg.connect(dbname=kwargs['dbname'], user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'], autocommit=kwargs['auto_commit'])
    print("Opened database successfully")
    
    print("Operation done successfully")
    return conn


#def execute(exe,dbname="",user_name="",pw="",ht="",prt=""):
def execute(exe,**kwargs):
    conn = connect2psql(**kwargs)
    cur = conn.cursor()
    if (kwargs['psql_script']):
        cur.execute(open(str(exe), "r").read()) 
    else: 
        cur.execute(exe)
    #NOTE: I commented this out because I wanted to check if my sql scripts are working out
    #NOTE: 09/22/2022
    if kwargs['output_name'] != None:
        wt.write_exe(kwargs['output_name'],cur.fetchall())
    else:
        print("If you want the results to your query, you must specify output_file name")
   
    cur.close()
    conn.close()



def csv2psql():
    print("csv2psql")


