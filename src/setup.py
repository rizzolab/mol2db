#!/usr/bin python3

#import necessary modules not-built in 
from setuptools import setup, Extension
from Cython.Build import cythonize



ext_modules = cythonize([
    Extension("mol2obj.mol2object", ["mol2obj/mol2object.py"]),
    Extension("mol2obj.utilities", ["mol2obj/utilities.py"]),
    Extension("write_mol.write_mol", ["write_mol/write_mol.py"]),
    Extension("psql_handeler.acc_psql", ["psql_handeler/acc_psql.py"])
    ],
    compiler_directives={'language_level' : "3"}
)

setup(
    ext_modules=ext_modules
)

