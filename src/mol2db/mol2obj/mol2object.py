#import built-in
import sys

#import self-made modules
#import mol2obj.utilities as ut
import mol2db.mol2obj.utilities as ut
from mol2db.write import write_csv as wc
from mol2db.write import write_mol as wm
from mol2db.parameters.headers import header_dict as hd


class Mol2obj:
    def __init__(self): #, atoms, bonds):
        self.atoms = {
                         "atom_num":  [],
                         "atom_name": [],
                         "x":         [],
                         "y":         [],
                         "z":         [],
                         "atom_type": [],
                         "subst_id":  [],
                         "subst_name":[], 
                         "charge":    [] 
                     } 

        self.bonds = {
                         "bond_num":    [],
                         "bond_first":  [],
                         "bond_second": [],
                         "bond_type":   []


                     } 
        self.num_atoms      = 0
        self.num_bonds      = 0
 
        # header attributes
        self.name           = ''
        self.mw             = 0.0
        self.rot_bond       = 0
        self.charge         = 0.0
        self.hba            = 0
        self.hbd            = 0
        self.heavy_atoms    = 0
        self.num_atom_rings = 0
        self.num_alip_rings = 0
        self.num_sat_rings  = 0
        self.num_stereo     = 0
        self.num_spiro      = 0
        self.logp           = 0.0
        self.tpsa           = 0.0
        self.syntha         = 0.0
        self.qed            = 0.0
        self.logs           = 0.0 
        self.num_pain       = 0.0
        self.pains_names    = ''
        self.smiles         = '' 
    ##getting name of molecule
    #def get_name(self):
    #    return f"{self.Name}"
    def __iter__(self):
        return self
    def get_attr(self):
        attr = []
        for attribute, value in self.__dict__.items():
            attr.append(attribute)
        return attr 

    def get_attr_val(self):
        attr = []
        for attribute, value in self.__dict__.items():
            attr.append(value)
        return attr

    def clear(self,not_none=False):
        attr = []
        for attribute, value in self.__dict__.items():
            attr.append(attribute)

        for att in attr:
            if "atoms" not in att or "bonds" not in att:
                if not_none == False:
                    setattr(self,att,None)
                else:
                    setattr(self,att,"NULL")
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
    #getting all atoms of molecules
    def get_atoms(self):
        return f"{self.atoms}" 

    #getting all atoms of molecules
    def get_bonds(self):
        return f"{self.bonds}"



##create an array of mol2objects
#def raw_to_objects(mol2s,objs):
#
#    tmp_atom_num  = []
#    tmp_atom_name = []
#    tmp_x         = []
#    tmp_y         = []
#    tmp_z         = []
#    tmp_atom_type = []
#    tmp_subst_id  = []
#    tmp_subst_name= []
#    tmp_charge    = []
#
#
#    tmp_bond_num    = []
#    tmp_bond_first  = []
#    tmp_bond_second = []
#    tmp_bond_type   = []
#    
#    headers   = ut.get_headers_names(mol2s)
#    
#    #get rid of the colon from the header labels
#    for i in range(len(headers)):
#        for j in range(len(headers[i])):
#            headers[i][j] = headers[i][j].replace(":","") 
#            #print(headers[i][j])
#
#
#
#    #iniate molecule and descriptor counters to access molecule headers
#    mol_count       = 0
#    des_count       = 0
#
#    #loop through the mol2 texts via line 
#    for i,line in enumerate(mol2s,0):
#        if (ut.if_header(line)):
#            if len(line.split()) != 3:
#                print("Line_"+str(i)+ ": missing descriptors or corrupted header line  " )
#                setattr(objs[mol_count],headers[mol_count][des_count],"NULL")
#            else:
#                #set attribute name, since the object as no set attributes, set the attributes here
#                setattr(objs[mol_count],headers[mol_count][des_count],line.split()[2])
#            #print(getattr(obj,headers[mol_count][des_count]))
#            des_count += 1
#
#        #if line is an atom line    
#        if (ut.if_atom(line)):
#            
#            tmp_atom_num.append(int(line.split()[0]))
#            tmp_atom_name.append(str(line.split()[1]))
#            tmp_x.append(float(line.split()[2]))         
#            tmp_y.append(float(line.split()[3]))         
#            tmp_z.append(float(line.split()[4]))         
#            tmp_atom_type.append(str(line.split()[5]))
#            tmp_subst_id.append(int(line.split()[6]))
#            tmp_subst_name.append(str(line.split()[7]))
#            tmp_charge.append(float(line.split()[-1]))
#    
#        #if line is an bond line
#        if (ut.if_bond(line)):
#            tmp_bond_num.append(int(line.split()[0]))
#            tmp_bond_first.append(int(line.split()[1]))
#            tmp_bond_second.append(int(line.split()[2]))
#            tmp_bond_type.append(str(line.split()[3]))
#
#
#
#
#
#        #End of molecule reset descriptor counter and increment mol_counter
#        if 'ROOT' in line:
#            #print("ROOT")
#            #insert tmp arrays into the dictionary attributes
#            objs[mol_count].atoms["atom_num"]    = tmp_atom_num        
#            objs[mol_count].atoms["atom_name"]   = tmp_atom_name
#            objs[mol_count].atoms["x"]           = tmp_x
#            objs[mol_count].atoms["y"]           = tmp_y       
#            objs[mol_count].atoms["z"]           = tmp_z
#            objs[mol_count].atoms["atom_type"]   = tmp_atom_type
#            objs[mol_count].atoms["subst_id"]    = tmp_subst_id
#            objs[mol_count].atoms["subst_name"]  = tmp_subst_name
#            objs[mol_count].atoms["charge"]      = tmp_charge
#           
#            objs[mol_count].bonds["bond_num"]    = tmp_bond_num
#            objs[mol_count].bonds["bond_first"]  = tmp_bond_first
#            objs[mol_count].bonds["bond_second"] = tmp_bond_second
#            objs[mol_count].bonds["bond_type"]   = tmp_bond_type
# 
#            objs[mol_count].num_atoms = len(tmp_atom_num)
#            objs[mol_count].num_bonds = len(tmp_bond_num)
#
#
#            #clear the tmp_atom and tmp_bond and iterate to the next molecule         
#            tmp_atom_num  = []
#            tmp_atom_name = []
#            tmp_x         = []
#            tmp_y         = []
#            tmp_z         = []
#            tmp_atom_type = []
#            tmp_subst_id  = []
#            tmp_subst_name= []
#            tmp_charge    = []
#
#            tmp_bond_num    = []
#            tmp_bond_first  = []
#            tmp_bond_second = []
#            tmp_bond_type   = []
#            mol_count += 1
#            des_count = 0


def mol2obj2write(mol2s,output_name):
    tmp_atom_num  = []
    tmp_atom_name = []
    tmp_x         = []
    tmp_y         = []
    tmp_z         = []
    tmp_atom_type = []
    tmp_subst_id  = []
    tmp_subst_name= []
    tmp_charge    = []


    tmp_bond_num    = []
    tmp_bond_first  = []
    tmp_bond_second = []
    tmp_bond_type   = []
   
    mol2_dict     = [] 

    headers   = ut.get_headers_names(mol2s)
 
    #get rid of the colon from the header labels
    for i in range(len(headers)):
        for j in range(len(headers[i])):
            headers[i][j] = headers[i][j].replace(":","")
            #print(headers[i][j])
    for l in headers:
        mol2_dict.append(ut.process_headers_names(l,hd))
    print(mol2_dict)

    #iniate molecule and descriptor counters to access molecule headers
    mol_count       = 0
    des_count       = 0
  
    obj = Mol2obj()

    #loop through the mol2 texts via line 
    for i,line in enumerate(mol2s,0):
        if (ut.if_header(line)):
            if len(line.split()) != 3:
                print("Line_"+str(i)+ ": missing descriptors or corrupted header line  " )
                setattr(obj,headers[mol_count][des_count],"NULL")
            else:
                #set attribute name, since the object as no set attributes, set the attributes here
                setattr(obj,headers[mol_count][des_count],line.split()[2])
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
            tmp_subst_id.append(int(line.split()[6]))
            tmp_subst_name.append(str(line.split()[7]))
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
            obj.atoms["atom_num"]    = tmp_atom_num
            obj.atoms["atom_name"]   = tmp_atom_name
            obj.atoms["x"]           = tmp_x
            obj.atoms["y"]           = tmp_y
            obj.atoms["z"]           = tmp_z
            obj.atoms["atom_type"]   = tmp_atom_type
            obj.atoms["subst_id"]    = tmp_subst_id
            obj.atoms["subst_name"]  = tmp_subst_name
            obj.atoms["charge"]      = tmp_charge

            obj.bonds["bond_num"]    = tmp_bond_num
            obj.bonds["bond_first"]  = tmp_bond_first
            obj.bonds["bond_second"] = tmp_bond_second
            obj.bonds["bond_type"]   = tmp_bond_type

            obj.num_atoms            = len(tmp_atom_num)
            obj.num_bonds            = len(tmp_bond_num)
           
            #write the python object 
            #wc.write_csv(output_name,obj)
            wm.write_mol(output_name,obj)

            #clear the tmp_atom and tmp_bond and iterate to the next molecule         
            tmp_atom_num  = []
            tmp_atom_name = []
            tmp_x         = []
            tmp_y         = []
            tmp_z         = []
            tmp_atom_type = []
            tmp_subst_id  = [] 
            tmp_subst_name= []
            tmp_charge    = []

            tmp_bond_num    = []
            tmp_bond_first  = []
            tmp_bond_second = []
            tmp_bond_type   = []
 
            obj.clear()
            #obj.atoms["atom_num"]    = tmp_atom_num
            #obj.atoms["atom_name"]   = tmp_atom_name
            #obj.atoms["x"]           = tmp_x
            #obj.atoms["y"]           = tmp_y
            #obj.atoms["z"]           = tmp_z
            #obj.atoms["atom_type"]   = tmp_atom_type
            #obj.atoms["charge"]      = tmp_charge

            #obj.bonds["bond_num"]    = tmp_bond_num
            #obj.bonds["bond_first"]  = tmp_bond_first
            #obj.bonds["bond_second"] = tmp_bond_second
            #obj.bonds["bond_type"]   = tmp_bond_type


            mol_count += 1
            des_count = 0
