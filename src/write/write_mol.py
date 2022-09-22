
#import built in
import csv


#write one mol at a time
def write_mol (output_name, mol):

    #if user did specify name use that name
    if (output_name != None):
        with open (output_name, 'a') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            row = []
            row = mol.get_attr_val()
            wr.writerow(row)
    #else use a default name
    else:
        with open ('mol2db.csv', 'a') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            row = []
            row = mol.get_attr_val()
            wr.writerow(row)


def write_mols (output_name, mols):
    if (output_name != None):
        with open (output_name, 'a') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for mol in mols:
                row = []
                row = mol.get_attr_val()
                wr.writerow(row)
    #else use a default name
    else:
        with open ('mol2db.csv', 'a') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            for mol in mols:
                row = []
                row = mol.get_attr_val()
                wr.writerow(row)



