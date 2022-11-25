
#import built in
import csv
import json


#write one mol at a time
def write_csv (output_name, mol):

    #if user did specify name use that name
    if (output_name != None):
        with open (output_name, 'a') as write_output:
            wr= csv.writer(write_output, delimiter='|', quoting=csv.QUOTE_MINIMAL,escapechar='"')
            row = []
            row = mol.get_attr_val()
            # row[0]=json.dumps(row[0])
            # row[1]=json.dumps(row[1])
            row[0]=json.dumps(mol.atoms)
            row[1]=json.dumps(mol.bonds)
            wr.writerow(row)
    #else use a default name
    else:
        with open ('mol2db.csv', 'a') as write_output:
            wr= csv.writer(write_output, delimiter='|', quoting=csv.QUOTE_MINIMAL,escapechar='"')
            row = []
            row = mol.get_attr_val()
             
            # row[0]=json.dumps(row[0])
            # row[1]=json.dumps(row[1])
            print(mol.atoms)
            row[0]=json.dumps(mol.atoms.atom_num)
            row[1]=json.dumps(mol.bonds)
            wr.writerow(row)


def write_csvs (output_name, mols):
    if (output_name != None):
        with open (output_name, 'a') as write_output:
            wr= csv.writer(write_output, delimiter='|', quoting=csv.QUOTE_NONE)
            for mol in mols:
                row = []
                row = mol.get_attr_val()
                wr.writerow(row)
    #else use a default name
    else:
        with open ('mol2db.csv', 'a') as write_output:
            wr= csv.writer(write_output, delimiter='|', quoting=csv.QUOTE_NONE)
            for mol in mols:
                row = []
                row = mol.get_attr_val()
                wr.writerow(row)



