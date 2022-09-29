#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    name='mol2db',
    version='0.1.0',    
    description='A molecule library handeler',
    url='https://github.com/Pakman450/mol2db',
    author='Steven Pak',
    author_email='steven.pak10@gmail.com',    
    license='MIT license',
    #src is where all of the devloping code is
    packages=find_packages('src'),
    package_dir={'': 'src'},
    #py_modules=["main","mol2obj/mol2object"],
    #
    include_package_data=True,
    install_requires=['Cython','psycopg','pandas'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)  
