
#import psycopg2, which is a python psql interfacing program
import psycopg2



def connect2psql (db_name,user_name,pw,ht,prt):
    conn = psycopg2.connect(database=db_name, user = user_name, password = pw, host = ht, port = prt)
    print("Opened database successfully")
