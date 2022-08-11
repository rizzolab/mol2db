#! /usr/bin/python

#import dockmol class
import mol2object as mol2obj

#import other functions
import utilities as ut 
import mol2_to_json as m2jn

#import built-in python modules
import sys
import argparse


#where we specify input parameters
parser = argparse.ArgumentParser()
parser.add_argument('-i',dest='raw_mol2',required=True, help="Feed a raw mol2 file here")
parser.add_argument('-o',dest='processed_csv', help="Name output csv file here")
args = parser.parse_args()


#give the path of the mol2 you want to process
input_mol2  = args.raw_mol2
output_name = args.processed_csv


##example dockmol object
#a = mol2obj.Mol2obj("name1",{'ESOL': 4.2, 'LOGP': 4.5})
#print(a.get_name())
#print(a.get_headers())


#read in the input_mol2 file
with open (input_mol2,'r') as mol2_file:
    read_files = mol2_file.readlines()

#first input the mol2 file into the mol2object

mol2objects = []
mol2objects = mol2obj.raw_to_objects(read_files)
#print(mol2objects)








number_col_list = ut.calculate_num_rows(read_files)

tmp_list=[]
for i,num in enumerate(number_col_list,0):
    tmp_list.append(number_col_list[i][1])
#print(number_col_list)
















#if user did specify name use that name
if (output_name != None): 
    with open (args.processed_csv, 'w') as write_output:
        for line in number_col_list:
            write_output.writelines(str(line)+'\n')
#else use a default name
else:
    with open ('mol2db.csv', 'w') as write_output:
        for line in number_col_list:
            write_output.writelines(str(line)+'\n')
