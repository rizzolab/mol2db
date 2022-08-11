import utilities as ut
import sys

class Mol2obj:

    def __init__(self): #, atoms, bonds):

    #getting name of molecule
    def get_name(self):
        return f"{self.name}"
    #getting all headers of molecule
    def get_headers(self):
        return f"{self.headers}"
   
    #getting all atoms of molecules
    def get_atoms():
        return f"{self.atoms}" 



#create an array of mol2objects
def raw_to_objects(mol2s):
    obj       = Mol2obj()
    objs      = []
    tmp_dict  = {}
    
    headers   = ut.get_headers_names(mol2s)
    
    #get rid of the colon from the header labels
    for i in range(len(headers)):
        for j in range(len(headers[i])):
            headers[i][j] = headers[i][j].replace(":","") 
            print(headers[i][j])


    mol_count       = 0
    des_count       = 0
    for i,line in enumerate(mol2s,0):
        if (ut.if_header(line)):
            setattr(obj,headers[mol_count][des_count],line.split()[2])
            print(getattr(obj,headers[mol_count][des_count]))
            print(obj.Name)
            des_count += 1
                
        if 'ROOT' in line:
            objs.append(obj) 
            mol_count += 1
            des_count = 0
                    
    return objs
