#! /usr/bin/python3
#import built-in python modules
import sys
import argparse
import csv
import time

#import dockmol class
from mol2obj import mol2object as mol2obj

#import other functions
from mol2obj import utilities as ut
from write_mol import write_mol as wm
from psql_handeler import acc_psql as ap 
from psql_handeler import iniatedb as ib
from argument_handeler import kwargs as kw 

#start time
start_time = time.time()

#where we specify input parameters
parser = argparse.ArgumentParser(prog='mol2db')
subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")


#arguments pertaining to only mol2csv
command_mol2csv = subparsers.add_parser('mol2csv', help='to convert molecules into csv')
command_mol2csv.add_argument('-i',dest='input',required=True, help="input a mol2 script")
command_mol2csv.add_argument('-o',dest='name_csv', help="Feed output file name")
command_mol2csv.add_argument('--null',dest='not_none', action="store_true",help="output in the csv to have NULL, instead of being empty")

#arguments pertaining to only str2exe 
command_str2exe = subparsers.add_parser('str2exe', help='to execute a sql string')
command_str2exe.add_argument('-i',dest='input',required=True, help="input a mol2 script")

command_str2exe.add_argument('-d','--dbname',dest='dbname',help="enter your database name to access")
command_str2exe.add_argument('-ur','--user' ,dest='user_name',help="enter your user name")
command_str2exe.add_argument('-pw','--pw'   ,dest='pw',help="enter your password")
command_str2exe.add_argument('-ht','--host' ,dest='ht',help="enter your host")
command_str2exe.add_argument('-pt','--prt' ,dest='prt',help="enter your port number")

#arguments pertaining to csv2psql
command_csv2psql = subparsers.add_parser('csv2psql', help='to load up csv into db')
command_csv2psql.add_argument('-i',dest='input',required=True, help="input your csv file")
command_csv2psql.add_argument('-t','--type',dest='csv_type',required=True,help="to know what set of molecule format")


#arguements pertaining to iniatedb
command_iniatedb = subparsers.add_parser('initiate', help='to create your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing psql. Then it will create the dbname of your choice. Please do not delete or change that name')
command_iniatedb.add_argument(dest='input', help="input your name of db")

command_iniatedb.add_argument('-ur','--user' ,dest='user_name',help="enter your user name")
command_iniatedb.add_argument('-pw','--pw'   ,dest='pw',help="enter your password")
command_iniatedb.add_argument('-ht','--host' ,dest='ht',help="enter your host")
command_iniatedb.add_argument('-pt','--prt'  ,dest='prt',help="enter your port number")


#arguements pertaining to deletedb
command_deletedb = subparsers.add_parser('delete', help='to delete your own db. This command will initially connect db named "postgres" under your username. This should be created by default when installing psql. Then it will create the dbname of your choice. Please do not delete or change that name')
command_deletedb.add_argument(dest='input', help="input your name of db")

command_deletedb.add_argument('-ur','--user' ,dest='user_name',help="enter your user name")
command_deletedb.add_argument('-pw','--pw'   ,dest='pw',help="enter your password")
command_deletedb.add_argument('-ht','--host' ,dest='ht',help="enter your host")
command_deletedb.add_argument('-pt','--prt'  ,dest='prt',help="enter your port number")

#make args object
args = parser.parse_args()

#preparing kwargs with args 
kwargs = kw.handle_kwargs(args)

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
   

elif (args.subcommand == "str2exe"):
    psql_exe = args.input
    
    ap.execute(psql_exe,**kwargs)
    

elif (args.subcommand == "csv2psql"):
    input_csv   = args.input

elif (args.subcommand == "initiate"):
    ib.iniatedb(args.input,**kwargs) 
elif (args.subcommand == "delete"):
    ib.deletedb(args.input,**kwargs)



end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")

