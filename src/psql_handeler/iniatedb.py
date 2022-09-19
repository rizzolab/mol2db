#This module creates a db with a specified name
import psycopg


def iniatedb(**kwargs):

    conn = psycopg.connect(dbname=kwargs['postgres'], user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'])

    print("Opened database successfully")
