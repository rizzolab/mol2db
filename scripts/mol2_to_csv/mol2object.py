#import self-made modules
import utilities as ut


#import built-in
import sys

class Mol2obj:
    def __init__(self): #, atoms, bonds):
        self.atoms = {
                         "atom_num":  [],
                         "atom_name": [],
                         "x":         [],
                         "y":         [],
                         "z":         [],
                         "atom_type": [],
                         "charge":    [] 
                     } 

        self.bonds = {
                         "bond_num":    [],
                         "bond_first":  [],
                         "bond_second": [],
                         "bond_type":   []
                     } 
    ##getting name of molecule
    #def get_name(self):
    #    return f"{self.name}"
    ##getting all headers of molecule
    #def get_headers(self):
    #    return f"{self.headers}"
    def get_attr(self):
        attr = []
        lol = dir(self) 
        print(lol)
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)
 
        return attr 

    def clear(self):
        self.atoms.clear()
        self.bonds.clear()
    #getting all atoms of molecules
    def get_atoms(self):
        return f"{self.atoms}" 

    #getting all atoms of molecules
    def get_bonds(self):
        return f"{self.bonds}"



#create an array of mol2objects
def raw_to_objects(mol2s,objs):

    tmp_atom_num  = []
    tmp_atom_name = []
    tmp_x         = []
    tmp_y         = []
    tmp_z         = []
    tmp_atom_type = []
    tmp_charge    = []


    tmp_bond_num    = []
    tmp_bond_first  = []
    tmp_bond_second = []
    tmp_bond_type   = []
    
    headers   = ut.get_headers_names(mol2s)
    
    #get rid of the colon from the header labels
    for i in range(len(headers)):
        for j in range(len(headers[i])):
            headers[i][j] = headers[i][j].replace(":","") 
            #print(headers[i][j])



    #iniate molecule and descriptor counters to access molecule headers
    mol_count       = 0
    des_count       = 0

    #loop through the mol2 texts via line 
    for i,line in enumerate(mol2s,0):
        if (ut.if_header(line)):
            if len(line.split()) != 3:
                print("Line_"+str(i)+ ": missing descriptors or corrupted header line  " )
                setattr(objs[mol_count],headers[mol_count][des_count],"NULL")
            else:
                #set attribute name, since the object as no set attributes, set the attributes here
                setattr(objs[mol_count],headers[mol_count][des_count],line.split()[2])
            #print(getattr(obj,headers[mol_count][des_count]))
            des_count += 1

        #if line is an atom line    
        if (ut.if_atom(line)):
            
            tmp_atom_num.append(int(line.split()[0]))
            tmp_atom_name.append(str(line.split()[1]))
            tmp_x.append(float(line.split()[2]))         
            tmp_y.append(float(line.split()[3]))         
            tmp_z.append(float(line.split()[4]))         
            tmp_atom_type.append(str(line.split()[5]))
            tmp_charge.append(float(line.split()[-1]))
    
        #if line is an bond line
        if (ut.if_bond(line)):
            tmp_bond_num.append(int(line.split()[0]))
            tmp_bond_first.append(int(line.split()[1]))
            tmp_bond_second.append(int(line.split()[2]))
            tmp_bond_type.append(str(line.split()[3]))

        #End of molecule reset descriptor counter and increment mol_counter
        if 'ROOT' in line:
            #print("ROOT")
            #insert tmp arrays into the dictionary attributes
            objs[mol_count].atoms["atom_num"]    = tmp_atom_num        
            objs[mol_count].atoms["atom_name"]   = tmp_atom_name
            objs[mol_count].atoms["x"]           = tmp_x
            objs[mol_count].atoms["y"]           = tmp_y       
            objs[mol_count].atoms["z"]           = tmp_z
            objs[mol_count].atoms["atom_type"]   = tmp_atom_type
            objs[mol_count].atoms["charge"]      = tmp_charge
           
            objs[mol_count].bonds["bond_num"]    = tmp_bond_num
            objs[mol_count].bonds["bond_first"]  = tmp_bond_first
            objs[mol_count].bonds["bond_second"] = tmp_bond_second
            objs[mol_count].bonds["bond_type"]   = tmp_bond_type


            #clear the tmp_atom and tmp_bond and iterate to the next molecule         
            tmp_atom_num  = []
            tmp_atom_name = []
            tmp_x         = []
            tmp_y         = []
            tmp_z         = []
            tmp_atom_type = []
            tmp_charge    = []

            tmp_bond_num    = []
            tmp_bond_first  = []
            tmp_bond_second = []
            tmp_bond_type   = []
            mol_count += 1
            des_count = 0
