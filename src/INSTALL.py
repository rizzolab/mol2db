import PyInstaller.__main__
import os

DIRNAME = os.path.dirname(__file__) + '/'

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    #'--clean',
    #'--add-data=./mol2db/config/mol2db.cred:./mol2db/config/',
    #'--paths='+DIRNAME
])
