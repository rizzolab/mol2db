#! /usr/bin/python

#import dockmol class
import dockmol

#import other functions
import mol2_to_csv as m2c 


#import built-in python modules
import sys

input_mol2 = sys.argv[1]

a = dockmol.Dockmol("name1",{'ESOL': '4.2', 'LOGP': '4.5'})
print(a.get_name())
print(a.get_headers())


read_files = []
#read in the input_mol2 file
with open (input_mol2,'r') as mol2_file:
    read_files = mol2_file.readlines()



number_col_list = m2c.calculate_num_rows(read_files)

tmp_list=[]
for i,num in enumerate(number_col_list,0):
    tmp_list.append(number_col_list[i][1])
print(number_col_list)
