import sys
import csv

# import psycopg, which is a python psql interfacing program
import psycopg

# import pandas
import pandas as pd

import numpy as np

from mol2db.write import write_exe as wt
from mol2db.write import write_mol as wm
from mol2db.mol2obj import mol2object as m2o

# from mol2db.sql_scripts import sql_script as ss

connected_withpsql = "Connected with db:"


def connect2psql(**kwargs):
    conn = psycopg.connect(
        dbname=kwargs["dbname"],
        user=kwargs["user_name"],
        password=kwargs["pw"],
        host=kwargs["ht"],
        port=kwargs["prt"],
        autocommit=kwargs["auto_commit"],
    )
    print(str_connect2psql(**kwargs))
    return conn


def str_connect2psql(**kwargs):
    i_dbname = kwargs["dbname"]
    return f"{connected_withpsql} {i_dbname}"


def execute(exe, **kwargs):
    conn = connect2psql(**kwargs)

    with conn.cursor() as cur:
        if "psql_script" in kwargs:
            if kwargs["psql_script"] == False:
                cur.execute(exe)
            else:
                cur.execute(open(str(exe), "r").read())
        elif "input_csv" in kwargs:
            path = kwargs["input_csv"]

            # read in csv file setting header and na_filter to False
            # na_filter is set to False because we want to create an empty string for the .replace() func
            df = pd.read_csv(path, delimiter="|", header=None, na_filter=False)

            # to replace all empty strings with None value so it can be pass
            # through psql tables
            df.replace(to_replace="", value=None, inplace=True)

            # import an iteratable tuple (row) into the psql database
            with cur.copy("COPY molecules FROM STDIN ") as copy:
                for ir in df.itertuples(index=False, name=None):
                    copy.write_row(ir)
                    continue
        else:
            cur.execute(exe)

        if "output_name" in kwargs:
            if kwargs["output_name"] != None:
                wt.write_exe(kwargs["output_name"], cur.fetchall())
            else:
                for i, line in enumerate(cur.fetchall(), 0):
                    print(str(i) + " RESULTS: " + str(line))
                print(
                    "If you want the results to query to an output file, you must specify output_file name"
                )

    cur.close()

    try:
        conn.close()
        print("Closed database successfully")
    except:
        sys.exit(
            "EXIT: ERROR in closing database. Please double check on your psql set up"
        )


def csv2psql():
    print("csv2psql")


# creating and deleting databases
def initiatedb(**kwargs):
    i_dbname = kwargs["DB_NAME"]
    conn = connect2psql(**kwargs, autocommit=True)
    cur = conn.cursor()
    try:
        cur.execute("CREATE DATABASE " + i_dbname)
    except psycopg.errors.DuplicateDatabase:
        conn.close()
        sys.exit(f"EXIT: database {i_dbname} already exists")
    print(i_dbname + " db was created")


def deletedb(**kwargs):
    i_dbname = kwargs["DB_NAME"]
    conn = connect2psql(**kwargs, autocommit=True)
    cur = conn.cursor()
    try:
        cur.execute("DROP DATABASE " + i_dbname)
    except psycopg.errors.InvalidCatalogName:
        conn.close()
        sys.exit(f"EXIT: database {i_dbname} does not exist")
    conn.close()
    print(i_dbname + " db was deleted")


def ifex(exe, **kwargs):
    i_dbname = kwargs["dbname"]
    conn = connect2psql(**kwargs, autocommit=True)
    cur = conn.cursor()
    cur.execute(exe)
    for i, line in enumerate(cur.fetchall(), 0):
        if True in line:
            print(
                "Table named "
                + kwargs["component"]
                + " does exists in "
                + kwargs["dbname"]
            )
        else:
            print(
                "Table named "
                + kwargs["component"]
                + " does not exists in "
                + kwargs["dbname"]
            )
    conn.close()


def pull_mols(exe, **kwargs):
    conn = connect2psql(**kwargs, autocommit=True)
    cur = conn.cursor()
    cur.execute(exe)

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        sys.exit(
            "EXIT: Nothing was pulled out. Check out the contents of your molecular table.\n"
            + "Make sure you are specifying the correct database and table"
        )

    for i, line in enumerate(cur.fetchall(), 0):
        m2o.curline2mol2write(line, kwargs["output_name"])

    cur.close()
    conn.close()


def pull_by_range(exe, **kwargs):
    conn = connect2psql(**kwargs, autocommit=True)
    print("Opened database successfully. Connected with postgres db")
