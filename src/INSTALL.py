import PyInstaller.__main__
import os

DIRNAME = os.path.dirname(__file__) + "/"

PyInstaller.__main__.run(
    [
        "m2db.py",
        "--onedir",
	"--distpath=./m2db",
        #'--clean',
        #'--add-data=./mol2db/config/mol2db.cred:./mol2db/config/',
        #'--paths='+DIRNAME
    ]
)
