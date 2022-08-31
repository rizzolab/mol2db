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

#start time
start_time = time.time()

#where we specify input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--job',dest='job',required=True, help="Feed the job type")
parser.add_argument('-i',dest='input',required=True, help="PATH to input")


#arguments pertaining to only mol2csv
parser.add_argument('-o',dest='name_csv', help="Feed output file name")
parser.add_argument('--null',dest='not_none', action="store_true",help="output in the csv to have NULL, instead of being empty")


#arguements pertaining to csv2psql



#make args object
args = parser.parse_args()


##decision tree here
#if (args.job == "mol2csv"):

#give the path of the mol2 you want to process
#SELECTED_JOB: raw mol2 to csv file for importation into the library 
if (args.job == "mol2csv"):
    input_mol2  = args.input
    output_name = args.name_csv
    #read in the input_mol2 file
    with open (input_mol2,'r') as mol2_file:
        read_files = mol2_file.readlines()
    
    #first input the mol2 file into the mol2object

    ##calculate the #num of mol
    #num_mol = 0
    #num_mol = ut.calc_num_mol(read_files)

    ##create num_mol number of mol2objs
    #mol2objects = [mol2obj.Mol2obj() for _ in range(num_mol)]
    
    ##convert mol2 file into mol2objects and write them into .mol2 files
    mol2obj.mol2obj2write(read_files,output_name)
   


elif (args.job == "csv2psql"):
    input_csv   = args.input



end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")

