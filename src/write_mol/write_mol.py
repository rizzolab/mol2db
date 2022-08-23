


def write_mol (output_name, mol):

    #if user did specify name use that name
    if (output_name != None):
        with open (args.name_csv, 'w') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            row = []
            row = mol.get_attr()
            wr.writerow(row)
    #else use a default name
    else:
        with open ('mol2db.csv', 'w') as write_output:
            wr= csv.writer(write_output, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            row = []
            row = mol.get_attr()
            wr.writerow(row)


