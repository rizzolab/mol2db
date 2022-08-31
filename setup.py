from setuptools import setup

setup(
    name='mol2db',
    version='0.1.0',    
    description='A molecule library handeler',
    url='https://github.com/Pakman450/mol2db',
    author='Steven Pak',
    author_email='steven.pak10@gmail.com',    
    license='MIT license',
    packages=['mol2db'],
    install_requires=['Cython','psycopg2'],

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
