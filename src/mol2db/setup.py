#!/usr/bin python3

#import necessary modules not-built in 
from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext 


ext_modules = cythonize([
    Extension("mol2obj.mol2object", ["mol2obj/mol2object.pyx"]),
    Extension("mol2obj.utilities", ["mol2obj/utilities.pyx"]),
    Extension("write.write_exe", ["write/write_exe.pyx"]),
    Extension("write.write_csv", ["write/write_csv.pyx"]),
    Extension("write.write_mol", ["write/write_mol.pyx"]),
    Extension("sql_scripts.sql_script",["sql_scripts/sql_script.pyx"]),
    Extension("parameters.headers",["parameters/headers.pyx"]),
    Extension("psql_handeler.acc_psql", ["psql_handeler/acc_psql.pyx"]),
    ],
    compiler_directives={'language_level' : "3"}
)

setup(
    name = 'm2db', 
    cmdclass = {'build_ext': build_ext}, 
    ext_modules = ext_modules 
    ##ext_modules=ext_modules
    #ext_modules = cythonize(["*.py"],compiler_directives={'language_level' : "3"})
)

