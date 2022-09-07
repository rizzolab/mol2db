
#import psycopg, which is a python psql interfacing program
import psycopg



#def connect2psql (dbname="",user_name="",pw="",ht="",prt=""):
def connect2psql (**kwargs):

    conn = psycopg.connect(dbname=kwargs['dbname'], user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'])
    print("Opened database successfully")
    
    print("Operation done successfully")
    return conn


#def execute(exe,dbname="",user_name="",pw="",ht="",prt=""):
def execute(exe,**kwargs):



    conn = connect2psql(**kwargs)
    cur = conn.cursor()
    cur.execute(exe)
    rows = cur.fetchall()
    print(rows)
    conn.close()
    

def csv2psql():
    print("csv2psql")





#connect2psql("spak","spak","KapSat2400180000","/var/run/postgresql","5432")
#connect2psql("SELECT * FROM example;",db_name="spak",user_name="spak")
