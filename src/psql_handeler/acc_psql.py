
#import psycopg, which is a python psql interfacing program
import psycopg

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
        print(cur.fetchall())
    else: 
        cur.execute(exe)
        print(cur.fetchall())

    cur.close()
    conn.close()



def csv2psql():
    print("csv2psql")


