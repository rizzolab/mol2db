#import builtin
import sys,os
import argparse
import time


#import other functions
from mol2db.mol2obj import mol2object as mol2obj
from mol2db.config import configure as cf
from mol2con.pullby import pullby as pb 

#start time
start_time = time.time()


#where we specify input parameters
parser = argparse.ArgumentParser(prog='mol2con')

#turn on verbose
parser.add_argument('-v',dest='verbose',action="store_true",help="add verbose func")


#arguments pertaining to pull_by_des
subparsers = parser.add_subparsers(help='help for subcommand', dest="subcommand")

#subcommands
command_pull_by_des = subparsers.add_parser('filter_by_des',help='to filter out molecules based on descriptor range')
command_pull_by_des.add_argument(dest='des', help="enter your descriptor")
command_pull_by_des.add_argument(dest='ope', help="available operators [more, emore, equal, less, eless] \
                                                   to choose from.")
command_pull_by_des.add_argument(dest='range', help="set the range")
command_pull_by_des.add_argument('-i',dest='input',required=True, help="input a mol2 file")
command_pull_by_des.add_argument('-o',dest='output_name', help="output_name")



#make args object
args = parser.parse_args()

#preparing kwargs with args 
kwargs = {}
kwargs= cf.make_kwargs(args)


#if verbose is turned on:
#display all of the parameters
if args.verbose:
    print("############################")
    print("Parameters used:")
    print("############################")
    for key,val in kwargs.items():
        print(str(key)+": " + str(val))
    print("############################")



##decision tree here
if (args.subcommand == "filter_by_des"):
    input_mol2  = kwargs['input']
    output_name = kwargs['output_name']

    with open('two.mol2','r') as mol2:
        readlines = mol2.readlines()
        pb.select_by_des(readlines)


end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")
