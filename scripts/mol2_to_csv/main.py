#! /usr/bin/python

#import dockmol class
import mol2object as mol2obj

#import other functions
import utilities as ut 

#import built-in python modules
import sys
import argparse
import csv


#where we specify input parameters
parser = argparse.ArgumentParser()
parser.add_argument('-i',dest='raw_mol2',required=True, help="Feed a raw mol2 file here")
parser.add_argument('-o',dest='processed_csv', help="Name output csv file here")
args = parser.parse_args()


#give the path of the mol2 you want to process
input_mol2  = args.raw_mol2
output_name = args.processed_csv


#read in the input_mol2 file
with open (input_mol2,'r') as mol2_file:
    read_files = mol2_file.readlines()

#first input the mol2 file into the mol2object
num_mol = 0
for line in read_files:
    if "MOLECULE" in line:
        num_mol +=1
mol2objects = [mol2obj.Mol2obj() for _ in range(num_mol)] 
mol2obj.raw_to_objects(read_files,mol2objects)


#if user did specify name use that name
if (output_name != None): 
    with open (args.processed_csv, 'w') as write_output:
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
