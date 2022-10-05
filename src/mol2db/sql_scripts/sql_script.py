#import built-in
import sys


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
