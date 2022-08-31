
#import psycopg, which is a python psql interfacing program
import psycopg



def connect2psql (db_name="",user_name="",pw="",ht="",prt=""):
    conn = psycopg.connect(dbname=db_name, user = user_name, password = pw,host = ht, port = prt)
    print("Opened database successfully")
    
    print("Operation done successfully")
    return conn


def execute(exe,db_name="",user_name="",pw="",ht="",prt=""):
    #NOTES: this next line is empty because now I realise there is a lot of passing of many arguments.
    #NOTES: through many passing of functions
    #NOTES: 08/31/2022
    conn = connect2psql()
    cur = conn.cursor()
    cur.execute(exe)
    rows = cur.fetchall()
    print(rows)
    conn.close()
    


#connect2psql("spak","spak","KapSat2400180000","/var/run/postgresql","5432")
#connect2psql("SELECT * FROM example;",db_name="spak",user_name="spak")
