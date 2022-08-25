# mol2db


#requirements
Cython is required to install this build. 
Cython is a program where it converts python code into C-code so it can be compiled into C code later

` 
pip install Cython
`


Current installation

`
cython -3 --embed main.py -o main.c
gcc -Os -I /usr/include/python3.9/ -o main main.c -lpython3.9 -lpthread -lm -lutil -ldl

`

This should output a binary named main
