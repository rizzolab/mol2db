from mol2db.parameters.headers import header_dict_reverse as hdr

def write_mol(output_name,mol):

    output_name = 'output.mol2' 

    with open(output_name,'a') as write_file: 

        #using f string to fill the atom_string
   
        #NOTE: saving this to write out the header information for write_mol
        hashT = "##########"

        header_string  = f''
        for key,value in hdr.items():
            header_string += f"{hashT:{22}}{value:>25}:{getattr(mol,key):>20}\n"       

        atom_string = f'' 
        for num in range(0,mol.num_atoms):
            atom_string += f"{mol.atoms['atom_num'][num]:{7}} "
            atom_string += f" {mol.atoms['atom_name'][num]:<4} " 
            atom_string += f" {mol.atoms['x'][num]:{12}.{4}f}"
            atom_string += f" {mol.atoms['y'][num]:{9}.{4}f}"
            atom_string += f" {mol.atoms['z'][num]:{9}.{4}f}"
            atom_string += f" {mol.atoms['atom_type'][num]:<5}"
            atom_string += f" {mol.atoms['subst_id'][num]:>2}"
            atom_string += f" {mol.atoms['subst_name'][num]:<16}"
            atom_string += f" {mol.atoms['charge'][num]:>7.{4}f}"
            atom_string += '\n'
        
        bond_string = f'' 
        for num in range(0,mol.num_bonds):
            bond_string += f"{mol.bonds['bond_num'][num]:{7}}"
            bond_string += f"{mol.bonds['bond_first'][num]:{6}}"
            bond_string += f"{mol.bonds['bond_second'][num]:{6}}"
            bond_string += f" {mol.bonds['bond_type'][num]:>4}"
            bond_string += '\n'
      
        mol_string = (
            header_string + '\n' +
            '@<TRIPOS>MOLECULE\n'+
            str(mol.name)+'\n'
            ' ' + str(len(mol.atoms["atom_num"])) + " " + str(len(mol.bonds["bond_num"])) + ' 1 0 0\n'
            'SMALL\n'
            'USER_CHARGES\n'
            '\n'
            '@<TRIPOS>ATOM\n'
            + atom_string + 
            '@<TRIPOS>BOND\n'
            + bond_string + 
            '@<TRIPOS>SUBSTRUCTURE\n'
            +'     1 <0>         1 TEMP              0 ****  ****    0 ROOT\n'
        )
        #write the mol in a mol2 format
        write_file.write(mol_string) 
