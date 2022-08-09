import utilities as ut

class Mol2obj:
    #def __init__(self, name,headers): #, atoms, bonds):
    #    self.name = name
    #    self.headers = headers
    #    #self.atoms = atoms
    #    #self.bonds = bonds 

    def __init__(self): #, atoms, bonds):
        self.name = ""
        self.MW   = 0
        self.descriptors = {}
    #getting name of molecule
    def get_name(self):
        return f"{self.name}"
    #getting all headers of molecule
    def get_headers(self):
        return f"{self.headers}"
   
    #getting all atoms of molecules
    def get_atoms():
        return f"{self.atoms}" 



##create a mol2object and bring back just one 
#def raw_to_object(mol2):
#    obj = Mol2obj()
#
#
#
#
#    return obj

#create an array of mol2objects
def raw_to_objects(mol2s):
    obj = Mol2obj()
    objs = []
    
    headers = ut.get_headers_names(mol2s)
    print(headers)


    mol_count = 0
    for line in mol2s:
        if (ut.if_header(line)):
            if ('Name:' in line and headers[mol_count]):
                obj.name = line.split()[2]
                print(obj.name)
            if ('Molecular_Weight:' in line and  headers[mol_count]):
                obj.MW   = line.split()[2]
                print(obj.MW)
        if 'ROOT' in line:
            mol_count += 1
                    



    return objs
