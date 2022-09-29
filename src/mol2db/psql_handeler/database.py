#This module creates a db with a specified name
import psycopg
from mol2db.psql_handeler import acc_psql as ap

def initiatedb(**kwargs):
    conn = ap.connect2psql(**kwargs,autocommit=True)
    #conn = psycopg.connect(dbname="postgres", user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'], autocommit=True)
    print("Opened database successfully. Connected with postgres db")
    cur = conn.cursor()
    i_dbname = kwargs['DB_NAME']
    cur.execute('CREATE DATABASE ' + i_dbname)  
    conn.close()
    print(i_dbname+' db was created')


def deletedb(**kwargs):   
    conn = ap.connect2psql(**kwargs,autocommit=True)
    #conn = psycopg.connect(dbname="postgres", user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'], autocommit=True)
    print("Opened database successfully. Connected with postgres db")
    cur = conn.cursor()
    i_dbname =kwargs['DB_NAME']
    cur.execute('DROP DATABASE ' + i_dbname)
    conn.close()
    print(i_dbname+' db was deleted')


