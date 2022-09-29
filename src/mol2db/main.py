#! /usr/bin/python3
#import built-in python modules
import sys
import os
import argparse
import csv
import time
import pkgutil

#import dockmol class
from mol2db.mol2obj import mol2object as mol2obj

#import other functions
from mol2db.mol2obj import utilities as ut
from mol2db.write import write_csv as wc
from mol2db.psql_handeler import acc_psql as ap 
from mol2db.psql_handeler import database as db
from mol2db.argument_handeler import kwargs as kw 
from mol2db.sql_scripts import sql_script as ss 

#create an object from SqlScripts
scripts = ss.SqlScripts()

#start time
start_time = time.time()

#where we specify input parameters
parser = argparse.ArgumentParser(prog='mol2db')

#Optional arguments flags
parser.add_argument('--autocommit',dest='auto_commit', action="store_true", help="specify if you want to autocommit(True) or not(False). No flag (False)")
parser.add_argument('-d','--dbname',dest='dbname',help="enter your database name to access")
parser.add_argument('-ur','--user' ,dest='user_name',help="enter your user name")
parser.add_argument('-pw','--pw'   ,dest='pw',help="enter your password")
parser.add_argument('-ht','--host' ,dest='ht',help="enter your host")
parser.add_argument('-pt','--prt'  ,dest='prt',help="enter your port number")

subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")

#arguments pertaining to only mol2csv
command_mol2csv = subparsers.add_parser('mol2csv', help='to convert molecules into csv')
command_mol2csv.add_argument('-i',dest='input',required=True, help="input a mol2 script")
command_mol2csv.add_argument('-o',dest='name_csv', help="Feed output file name")
command_mol2csv.add_argument('--null',dest='not_none', action="store_true",help="output in the csv to have NULL, instead of being empty")

#arguments pertaining to only execute 
command_str2exe = subparsers.add_parser('execute', help='to execute a sql string')
command_str2exe.add_argument(dest='str_2_exe', help="input string or psql script")
command_str2exe.add_argument('-o',dest='output_name', help="output_name")
command_str2exe.add_argument('-ps','--psql_script',dest='psql_script', action="store_true", help="specify if you want to sql script(True) or not(False). No flag (False)")


#arguments pertaining to csv2psql
command_csv2psql = subparsers.add_parser('csv2psql', help='to load up csv into db')
command_csv2psql.add_argument(dest='input_csv', help="input your csv file")

#arguments pertaining to moltables
command_moltables = subparsers.add_parser('moltables', help='to load up csv into db')

#arguements pertaining to iniatedb
command_iniatedb = subparsers.add_parser('create', help='to create your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing psql. Then it will create the dbname of your choice. Please do not delete or change that name')
command_iniatedb.add_argument(dest='DB_NAME', help="input your name of db")


#arguements pertaining to deletedb
command_deletedb = subparsers.add_parser('delete', help='to delete your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing psql. Then it will create the dbname of your choice. Please do not delete or change that name')
command_deletedb.add_argument(dest='DB_NAME', help="input your name of db")


#make args object
args = parser.parse_args()

#preparing kwargs with args 
kwargs = kw.handle_kwargs(args)

print(kwargs)
##decision tree here
#give the path of the mol2 you want to process
#SELECTED_JOB: raw mol2 to csv file for importation into the library 
if (args.subcommand == "mol2csv"):
    input_mol2  = kwargs['input']
    output_name = kwargs['name_csv']
    #read in the input_mol2 file
    with open (input_mol2,'r') as mol2_file:
        read_files = mol2_file.readlines()
    
    ##convert mol2 file into mol2objects and write them into .mol2 files
    mol2obj.mol2obj2write(read_files,output_name)

elif (args.subcommand == "execute"):
    ap.execute(args.str_2_exe,**kwargs)

elif (args.subcommand == "csv2psql"):
    input_csv = args.input_csv
    exe=""
    ap.execute(exe,**kwargs)

elif (args.subcommand == "moltables"):
    #exe = open(file_dir + '/sql_scripts/mol_tables.sql', "r").read()
    exe = scripts.molTables
    ap.execute(exe,**kwargs)
elif (args.subcommand == "create"):
    db.initiatedb(**kwargs) 

elif (args.subcommand == "delete"):
    db.deletedb(**kwargs)

end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")
