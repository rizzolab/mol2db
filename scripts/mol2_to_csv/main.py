#! /usr/bin/python

#import dockmol class
import mol2object as mol2obj

#import other functions
import utilities as ut 

#import built-in python modules
import sys
import argparse
import csv
import time


#start time
start_time = time.time()

#where we specify input parameters
parser = argparse.ArgumentParser()
parser.add_argument('-i',dest='raw_mol2',required=True, help="Feed a raw mol2 file here")
parser.add_argument('-o',dest='name_csv', help="Name output csv file here")
args = parser.parse_args()


#give the path of the mol2 you want to process
input_mol2  = args.raw_mol2
output_name = args.name_csv


#read in the input_mol2 file
with open (input_mol2,'r') as mol2_file:
    read_files = mol2_file.readlines()

#first input the mol2 file into the mol2object
num_mol = 0
for line in read_files:
    if "MOLECULE" in line:
        num_mol +=1
#create num_mol number of mol2objs
mol2objects = [mol2obj.Mol2obj() for _ in range(num_mol)] 

#convert mol2 file into mol2objects
mol2obj.raw_to_objects(read_files,mol2objects)


#if user did specify name use that name
if (output_name != None): 
    with open (args.name_csv, 'w') as write_output:
        for line in number_col_list:
            write_output.writelines(str(line)+'\n')
#else use a default name
else:
    with open ('mol2db.csv', 'w') as write_output:
        wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for mol in mol2objects:
            row = []
            row = mol.get_attr()
            wr.writerow(row)


end_time = time.time()
print('duration: ' + str(end_time - start_time)+ " seconds")

