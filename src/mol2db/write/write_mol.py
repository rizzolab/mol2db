

def write_mol(output_name,mol):

    output_name = 'output.mol2' 

    with open(output_name,'a') as write_file: 
        #write_file.write('@<TRIPOS>MOLECULE\n')
        #write_file.write(mol.Name+'\n')
        #write_file.write(' ' + str(len(mol.atoms["atom_num"])) + " " + str(len(mol.bonds["bond_num"])) + ' 1 0 0\n')
        #write_file.write('SMALL\n')
        #write_file.write('USER_CHARGES\n')
        #write_file.write('\n')
        #write_file.write('@<TRIPOS>ATOM\n')



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
            '@<TRIPOS>MOLECULE\n'+
            str(mol.Name)+'\n'
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






        
        write_file.write(mol_string) 
            
        



