# import built-in
import sys
import json

# import pandas
import pandas as pd

# import self-made modules
# import mol2obj.utilities as ut
from mol2db.mol2obj import utilities as ut
from mol2db.write import write_csv as wc
from mol2db.write import write_mol as wm
from mol2db.parameters.headers import header_dict as hd
from mol2db.mol2obj import atoms as at
from mol2db.mol2obj import bonds as bn


class Mol2obj:
    def __init__(self, mol2=None):
        self.atoms = at.atoms()
        self.bonds = bn.bonds()
        self.num_atoms = None
        self.num_bonds = None

        # header attributes
        self.name = None
        self.mw = None
        self.rot_bond = None
        self.charge = None
        self.hba = None
        self.hbd = None
        self.heavy_atoms = None
        self.num_atom_rings = None
        self.num_alip_rings = None
        self.num_sat_rings = None
        self.num_stereo = None
        self.num_spiro = None
        self.logp = None
        self.tpsa = None
        self.syntha = None
        self.qed = None
        self.logs = None
        self.num_pain = None
        self.pains_names = None

        self.smiles = None
        if mol2:
            self_mol2obj(self, mol2)

    ##getting name of molecule
    # def get_name(self):
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

    def clear(self, not_none=False):
        self.atoms.clear()
        self.bonds.clear()

        attr = []
        for attribute, value in self.__dict__.items():
            if attribute in ["atoms", "bonds"]:
                continue
            else:
                attr.append(attribute)

        for att in attr:
            if not_none == False:
                setattr(self, att, None)
            else:
                setattr(self, att, "NULL")

    # getting all atoms of molecules
    def get_atoms(self):
        return f"{self.atoms}"

    # getting all atoms of molecules
    def get_bonds(self):
        return f"{self.bonds}"


def self_mol2obj(self, mol2):
    tmp_atom_num = []
    tmp_atom_name = []
    tmp_x = []
    tmp_y = []
    tmp_z = []
    tmp_atom_type = []
    tmp_subst_id = []
    tmp_subst_name = []
    tmp_charge = []

    tmp_bond_num = []
    tmp_bond_first = []
    tmp_bond_second = []
    tmp_bond_type = []

    mol2_dict = []

    headers = ut.get_headers_names(mol2)

    # get rid of the colon from the header labels
    for i in range(len(headers)):
        for j in range(len(headers[i])):
            headers[i][j] = headers[i][j].replace(":", "")
    for l in headers:
        mol2_dict.append(ut.process_headers_names(l, hd))

    # iniate molecule and descriptor counters to access molecule headers
    mol_count = 0
    des_count = 0

    # loop through the mol2 texts via line
    for i, line in enumerate(mol2, 0):
        if ut.if_header(line):
            tmp_header_name = line.split()[1].replace(":", "")
            if mol2_dict[mol_count][hd[tmp_header_name]]:
                setattr(self, hd[tmp_header_name], line.split()[2])
            else:
                setattr(self, hd[tmp_header_name], None)

        # if line is an atom line
        if ut.if_atom(line):
            tmp_atom_num.append(int(line.split()[0]))
            tmp_atom_name.append(str(line.split()[1]))
            tmp_x.append(float(line.split()[2]))
            tmp_y.append(float(line.split()[3]))
            tmp_z.append(float(line.split()[4]))
            tmp_atom_type.append(str(line.split()[5]))
            tmp_subst_id.append(int(line.split()[6]))
            tmp_subst_name.append(str(line.split()[7]))
            tmp_charge.append(float(line.split()[-1]))

        # if line is an bond line
        if ut.if_bond(line):
            tmp_bond_num.append(int(line.split()[0]))
            tmp_bond_first.append(int(line.split()[1]))
            tmp_bond_second.append(int(line.split()[2]))
            tmp_bond_type.append(str(line.split()[3]))

        # End of molecule reset descriptor counter and increment mol_counter
        if "ROOT" in line:
            # insert tmp arrays into the dictionary attributes
            self.atoms.atom_num = tmp_atom_num
            self.atoms.atom_name = tmp_atom_name
            self.atoms.x = tmp_x
            self.atoms.y = tmp_y
            self.atoms.z = tmp_z
            self.atoms.atom_type = tmp_atom_type
            self.atoms.subst_id = tmp_subst_id
            self.atoms.subst_name = tmp_subst_name
            self.atoms.charge = tmp_charge

            self.bonds.bond_num = tmp_bond_num
            self.bonds.bond_first = tmp_bond_first
            self.bonds.bond_second = tmp_bond_second
            self.bonds.bond_type = tmp_bond_type

            self.num_atoms = len(tmp_atom_num)
            self.num_bonds = len(tmp_bond_num)

            # clear the tmp_atom and tmp_bond and iterate to the next molecule
            tmp_atom_num = []
            tmp_atom_name = []
            tmp_x = []
            tmp_y = []
            tmp_z = []
            tmp_atom_type = []
            tmp_subst_id = []
            tmp_subst_name = []
            tmp_charge = []

            tmp_bond_num = []
            tmp_bond_first = []
            tmp_bond_second = []
            tmp_bond_type = []

            mol_count += 1


def curline2mol2write(cur_line, output_name):
    tmp_atom_num = []
    tmp_atom_name = []
    tmp_x = []
    tmp_y = []
    tmp_z = []
    tmp_atom_type = []
    tmp_subst_id = []
    tmp_subst_name = []
    tmp_charge = []

    tmp_bond_num = []
    tmp_bond_first = []
    tmp_bond_second = []
    tmp_bond_type = []

    obj = Mol2obj()
    # access column of atoms information (coordinates, atom types, etc)

    ##if line is an atom line
    tmp_atom_num = cur_line[0]["atom_num"]
    tmp_atom_name = cur_line[0]["atom_name"]
    tmp_x = cur_line[0]["x"]
    tmp_y = cur_line[0]["y"]
    tmp_z = cur_line[0]["z"]
    tmp_atom_type = cur_line[0]["atom_type"]
    tmp_subst_id = cur_line[0]["subst_id"]
    tmp_subst_name = cur_line[0]["subst_name"]
    tmp_charge = cur_line[0]["charge"]

    ##if line is an bond line
    tmp_bond_num = cur_line[1]["bond_num"]
    tmp_bond_first = cur_line[1]["bond_first"]
    tmp_bond_second = cur_line[1]["bond_second"]
    tmp_bond_type = cur_line[1]["bond_type"]

    obj.atoms.atom_num = tmp_atom_num
    obj.atoms.atom_name = tmp_atom_name
    obj.atoms.x = tmp_x
    obj.atoms.y = tmp_y
    obj.atoms.z = tmp_z
    obj.atoms.atom_type = tmp_atom_type
    obj.atoms.subst_id = tmp_subst_id
    obj.atoms.subst_name = tmp_subst_name
    obj.atoms.charge = tmp_charge

    obj.bonds.bond_num = tmp_bond_num
    obj.bonds.bond_first = tmp_bond_first
    obj.bonds.bond_second = tmp_bond_second
    obj.bonds.bond_type = tmp_bond_type

    obj.num_atoms = len(tmp_atom_num)
    obj.num_bonds = len(tmp_bond_num)

    obj.name = cur_line[4]
    obj.mw = cur_line[5]
    obj.rot_bond = cur_line[6]
    obj.charge = cur_line[7]
    obj.hba = cur_line[8]
    obj.hbd = cur_line[9]
    obj.heavy_atoms = cur_line[10]
    obj.num_atom_rings = cur_line[11]
    obj.num_alip_rings = cur_line[12]
    obj.num_sat_rings = cur_line[13]
    obj.num_stereo = cur_line[14]
    obj.num_spiro = cur_line[15]
    obj.logp = cur_line[16]
    obj.tpsa = cur_line[17]
    obj.syntha = cur_line[18]
    obj.qed = cur_line[19]
    obj.logs = cur_line[20]
    obj.num_pain = cur_line[21]
    obj.pains_names = cur_line[22]
    obj.smiles = cur_line[23]

    wm.write_mol(output_name, obj)

    # clear the tmp_atom and tmp_bond and iterate to the next molecule
    tmp_atom_num = []
    tmp_atom_name = []
    tmp_x = []
    tmp_y = []
    tmp_z = []
    tmp_atom_type = []
    tmp_subst_id = []
    tmp_subst_name = []
    tmp_charge = []

    tmp_bond_num = []
    tmp_bond_first = []
    tmp_bond_second = []
    tmp_bond_type = []

    obj.clear()


def csv2mol2write(input_csv, output_name):
    df = pd.read_csv(input_csv, delimiter="|", header=None, na_filter=False)
    df.replace(to_replace="", value=None, inplace=True)

    tmp_atom_num = []
    tmp_atom_name = []
    tmp_x = []
    tmp_y = []
    tmp_z = []
    tmp_atom_type = []
    tmp_subst_id = []
    tmp_subst_name = []
    tmp_charge = []

    tmp_bond_num = []
    tmp_bond_first = []
    tmp_bond_second = []
    tmp_bond_type = []

    obj = Mol2obj()
    # access column of atoms information (coordinates, atom types, etc)
    for row_num in range(0, len(df)):
        ##if line is an atom line
        dict_atom = json.loads(df[0][row_num])
        tmp_atom_num = dict_atom["atom_num"]
        tmp_atom_name = dict_atom["atom_name"]
        tmp_x = dict_atom["x"]
        tmp_y = dict_atom["y"]
        tmp_z = dict_atom["z"]
        tmp_atom_type = dict_atom["atom_type"]
        tmp_subst_id = dict_atom["subst_id"]
        tmp_subst_name = dict_atom["subst_name"]
        tmp_charge = dict_atom["charge"]

        ##if line is an bond line
        dict_bond = json.loads(df[1][row_num])
        tmp_bond_num = dict_bond["bond_num"]
        tmp_bond_first = dict_bond["bond_first"]
        tmp_bond_second = dict_bond["bond_second"]
        tmp_bond_type = dict_bond["bond_type"]

        obj.atoms.atom_num = tmp_atom_num
        obj.atoms.atom_name = tmp_atom_name
        obj.atoms.x = tmp_x
        obj.atoms.y = tmp_y
        obj.atoms.z = tmp_z
        obj.atoms.atom_type = tmp_atom_type
        obj.atoms.subst_id = tmp_subst_id
        obj.atoms.subst_name = tmp_subst_name
        obj.atoms.charge = tmp_charge

        obj.bonds.bond_num = tmp_bond_num
        obj.bonds.bond_first = tmp_bond_first
        obj.bonds.bond_second = tmp_bond_second
        obj.bonds.bond_type = tmp_bond_type

        obj.num_atoms = len(tmp_atom_num)
        obj.num_bonds = len(tmp_bond_num)

        obj.name = df[4][row_num]
        obj.mw = df[5][row_num]
        obj.rot_bond = df[6][row_num]
        obj.charge = df[7][row_num]
        obj.hba = df[8][row_num]
        obj.hbd = df[9][row_num]
        obj.heavy_atoms = df[10][row_num]
        obj.num_atom_rings = df[11][row_num]
        obj.num_alip_rings = df[12][row_num]
        obj.num_sat_rings = df[13][row_num]
        obj.num_stereo = df[14][row_num]
        obj.num_spiro = df[15][row_num]
        obj.logp = df[16][row_num]
        obj.tpsa = df[17][row_num]
        obj.syntha = df[18][row_num]
        obj.qed = df[19][row_num]
        obj.logs = df[20][row_num]
        obj.num_pain = df[21][row_num]
        obj.pains_names = df[22][row_num]
        obj.smiles = df[23][row_num]

        wm.write_mol(output_name, obj)

        # clear the tmp_atom and tmp_bond and iterate to the next molecule
        tmp_atom_num = []
        tmp_atom_name = []
        tmp_x = []
        tmp_y = []
        tmp_z = []
        tmp_atom_type = []
        tmp_subst_id = []
        tmp_subst_name = []
        tmp_charge = []

        tmp_bond_num = []
        tmp_bond_first = []
        tmp_bond_second = []
        tmp_bond_type = []

        obj.clear()


def mol2obj2write(mol2s, output_name):
    tmp_atom_num = []
    tmp_atom_name = []
    tmp_x = []
    tmp_y = []
    tmp_z = []
    tmp_atom_type = []
    tmp_subst_id = []
    tmp_subst_name = []
    tmp_charge = []

    tmp_bond_num = []
    tmp_bond_first = []
    tmp_bond_second = []
    tmp_bond_type = []

    mol2_dict = []

    headers = ut.get_headers_names(mol2s)

    # get rid of the colon from the header labels
    for i in range(len(headers)):
        for j in range(len(headers[i])):
            headers[i][j] = headers[i][j].replace(":", "")
    for l in headers:
        mol2_dict.append(ut.process_headers_names(l, hd))

    # iniate molecule and descriptor counters to access molecule headers
    mol_count = 0
    des_count = 0

    obj = Mol2obj()

    # loop through the mol2 texts via line
    for i, line in enumerate(mol2s, 0):
        if ut.if_header(line):
            # for key,value in mol2_dict[i].items():
            tmp_header_name = line.split()[1].replace(":", "")
            if mol2_dict[mol_count][hd[tmp_header_name]]:
                setattr(obj, hd[tmp_header_name], line.split()[2])
            else:
                setattr(obj, hd[tmp_header_name], None)

        # if line is an atom line
        if ut.if_atom(line):
            tmp_atom_num.append(int(line.split()[0]))
            tmp_atom_name.append(str(line.split()[1]))
            tmp_x.append(float(line.split()[2]))
            tmp_y.append(float(line.split()[3]))
            tmp_z.append(float(line.split()[4]))
            tmp_atom_type.append(str(line.split()[5]))
            tmp_subst_id.append(int(line.split()[6]))
            tmp_subst_name.append(str(line.split()[7]))
            tmp_charge.append(float(line.split()[-1]))

        # if line is an bond line
        if ut.if_bond(line):
            tmp_bond_num.append(int(line.split()[0]))
            tmp_bond_first.append(int(line.split()[1]))
            tmp_bond_second.append(int(line.split()[2]))
            tmp_bond_type.append(str(line.split()[3]))

        # End of molecule reset descriptor counter and increment mol_counter
        if "ROOT" in line:
            # insert tmp arrays into the dictionary attributes
            obj.atoms.atom_num = tmp_atom_num
            obj.atoms.atom_name = tmp_atom_name
            obj.atoms.x = tmp_x
            obj.atoms.y = tmp_y
            obj.atoms.z = tmp_z
            obj.atoms.atom_type = tmp_atom_type
            obj.atoms.subst_id = tmp_subst_id
            obj.atoms.subst_name = tmp_subst_name
            obj.atoms.charge = tmp_charge

            obj.bonds.bond_num = tmp_bond_num
            obj.bonds.bond_first = tmp_bond_first
            obj.bonds.bond_second = tmp_bond_second
            obj.bonds.bond_type = tmp_bond_type

            obj.num_atoms = len(tmp_atom_num)
            obj.num_bonds = len(tmp_bond_num)

            # write the python object
            wc.write_csv(output_name, obj)

            # clear the tmp_atom and tmp_bond and iterate to the next molecule
            tmp_atom_num = []
            tmp_atom_name = []
            tmp_x = []
            tmp_y = []
            tmp_z = []
            tmp_atom_type = []
            tmp_subst_id = []
            tmp_subst_name = []
            tmp_charge = []

            tmp_bond_num = []
            tmp_bond_first = []
            tmp_bond_second = []
            tmp_bond_type = []

            obj.clear()

            mol_count += 1
