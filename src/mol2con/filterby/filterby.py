# import python build in
import sys
import operator


# get the mol2 object class
from mol2db.mol2obj import mol2object as mol2obj

# get writing class
from mol2db.write import write_mol as wm

# get header parameters
from mol2db.parameters import headers as hd
from mol2db.parameters import operators as op


def check_if_in_range(mol, **kwargs):
    if not kwargs["des"] or not kwargs["ope"] or not kwargs["range"]:
        sys.exit("input is not corrent")

    return op.ops[kwargs["ope"]](getattr(mol, kwargs["des"]), kwargs["range"])


def select_by_des(input_mol2, **kwargs):
    single_mol = []

    for i, line in enumerate(input_mol2, 0):
        single_mol.append(line)

        if "ROOT" in line:
            obj = mol2obj.Mol2obj(single_mol)
            if check_if_in_range(obj, **kwargs):
                wm.write_mol(kwargs["output_name"], obj)
            obj.clear()
            single_mol = []
