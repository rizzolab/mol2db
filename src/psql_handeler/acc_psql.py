
#import psycopg, which is a python psql interfacing program
import psycopg



#def connect2psql (db_name,user_name,pw,ht,prt):
def connect2psql (db_name,user_name,pw):
    print("lol1")
    conn = psycopg.connect(dbname=db_name, user = user_name, password = pw)
    print("Opened database successfully")
    print("lol")


connect2psql("spak","spak","KapSat2400180000")
