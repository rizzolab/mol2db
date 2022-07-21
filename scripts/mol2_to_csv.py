#! /usr/bin/python


#This script goal is to process a mol2 file into a csv file
#so it can be imported into a psql db

import sys
import csv
import time
start_time = time.time()
input_mol2 = sys.argv[1]



#this function accepts an array of elements and check each element is a
#float. If ONE of the elements is an integer it will immediately return False
def is_floatnumber(float_line):
    try:
        for line in float_line:
            float(line)   # Type-casting the string to `float`.
            if line.isdigit() == True:
                return False
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

#this function accepts an array of elements and check each element is a
#int. If ONE of the elements is an NOT an integer it will immediately return False
def is_intnumber(int_line):
    try:
        for line in int_line:
            if line.isdigit() == False:
                return False 
        return True 
    except:
       return False

#check if the string line means the atom
def if_atom(line):
   
    #Assume return_value is Flase until all is true

    return_value = False
    try:      
        if is_intnumber([line.split()[0]]) == True and is_floatnumber([line.split()[2],line.split()[3],line.split()[4]]) == True:
            return True
    except:
        return return_value 

#check if the string line means the bond
def if_bond(line):
    return_value = False
    try:
        if len(line.split()) == 4 and is_intnumber([line.split()[0],line.split()[1],line.split()[2]]):
            return True
    except:
        return return_value



#gather the the number of atoms and bonds in a molecule
def calculate_num_rows(mol2):

    #return_dict has [numOfDesCol], [numOfAtomCol], [numOfBondCol]
    return_list=[]
    
    #mol_count = 0
    des_count = 0
    atom_count = 0
    bond_count = 0
     
    for line in mol2:
        if len(line.split()) == 0:
            continue
        #print(line.split()[0])
        if '##########' in line:
            des_count += 1  
        print(line)
        if if_atom(line):
            atom_count += 1
            print('ATOM_LINE')
        if if_bond(line):
            bond_count += 1
        if 'ROOT' in line:
            #mol_count += 1
            return_list.append([des_count,atom_count,bond_count])
            des_count = 0 
            atom_count = 0 
            bond_count = 0

    return return_list


with open (input_mol2,'r') as mol2_file:
    read_files = mol2_file.readlines()

column_list = []
split_line = []
for line in read_files:
    if len(line.split()) == 0:
        continue
    elif '##########' in line.split()[0]:
        column_list.append(line.split()[1])


print(calculate_num_rows(read_files))







end_time = time.time()





