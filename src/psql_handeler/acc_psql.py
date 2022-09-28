
import csv
#import psycopg, which is a python psql interfacing program
import psycopg
#import pandas
import pandas as pd

from write import write_exe as wt


#def connect2psql (dbname="",user_name="",pw="",ht="",prt=""):
def connect2psql (**kwargs):

    conn = psycopg.connect(dbname=kwargs['dbname'], user = kwargs['user_name'], password = kwargs['pw'],host = kwargs['ht'], port = kwargs['prt'], autocommit=kwargs['auto_commit'])
    print("Opened database successfully")
    
    print("Operation done successfully")
    return conn


def execute(exe,**kwargs):
    conn = connect2psql(**kwargs)
    with conn.cursor() as cur:
    
        if 'psql_script' in kwargs: 
            if (kwargs['psql_script']== False):
                cur.execute(exe)
            else:
                cur.execute(open(str(exe), "r").read()) 
        elif 'input_csv' in kwargs:
            path = kwargs['input_csv']
            df = pd.read_csv(path,delimiter='|')

            with cur.copy("COPY molecules FROM STDIN ") as copy:
                for ir in df.itertuples(index=False,name=None):
                    copy.write_row(ir) 
              
        else:
            cur.execute(exe)

    if 'output_name' in kwargs:
        if kwargs['output_name'] != None:
            wt.write_exe(kwargs['output_name'],cur.fetchall())
        else:
            print("If you want the results to your query, you must specify output_file name")
   
    cur.close()
    conn.close()



def csv2psql():
    print("csv2psql")


