#import built-in
import sys
from mol2db.parameters import operators as op

class SqlScripts:
    def __init__(self):
        self.molTables = """CREATE TABLE molecules(
                              ATOMS JSON NOT NULL,
                              BONDS JSON NOT NULL,
                              NUM_ATOMS INT,
                              NUM_BONDS INT,
                              NAME TEXT PRIMARY KEY NOT NULL,
                              MW DECIMAL,
                              ROT_BONDS INT,
                              FORMAL_CHARGE DECIMAL,
                              HBA INT,
                              HBD INT,
                              HEAVY_ATOMS INT,
                              NUM_AROM INT,
                              NUM_ALIP INT,
                              NUM_SAT INT,
                              NUM_STEREO INT,
                              NUM_SPIRO INT,
                              LOGP DECIMAL,
                              TPSA DECIMAL,
                              SYNTHA DECIMAL,
                              QED DECIMAL,
                              LOGS DECIMAL,
                              NUM_PAINS INT,
                              PAINS_NAMES TEXT,
                              SMILES TEXT
                          );"""
    def ifex(self,db_name, table_name):
        return_ifex = " SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE " \
        " table_schema='public' AND table_name="\
        + "'"+table_name+"'" + ");"
        return return_ifex

    def pull_mols(self,input_file):
        names = "('"

        try:
            with open (input_file,'r') as zinc_file:
                read_files = zinc_file.readlines()
        except FileNotFoundError:
            print('Path of file cannot be found. adjust the path name')
            sys.exit('exiting...')

        for i,line in enumerate(read_files,0):
            if i+1 == len(read_files):
                names += line.strip('\n') +"')"
            else:
                names += line.strip('\n') +"','"
        return_name = f"SELECT * FROM molecules WHERE name in {names};"
        return return_name
    def pull_by_des(self,des,ope,set_range):
        sign = op.operators[ope] 
        return_exe = f"SELECT * FROM molecules WHERE {des} {sign} {set_range};"
        return return_exe
    def pull_by_range(self,des,lower,upper):
        return_exe = f"SELECT * FROM molecules WHERE {des} BETWEEN {lower} and {upper};"
        return return_exe
