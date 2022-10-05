# you can set your expected header information hear  
import pandas as pd

header_dict = {
                       "Name": "name"           ,
           "Molecular_Weight": "mw"             ,
       "DOCK_Rotatable_Bonds": "rot_bond"       ,
              "Formal_Charge": "charge"         ,
            "HBond_Acceptors": "hba"            ,
               "HBond_Donors": "hbd"            ,
                "Heavy_Atoms": "heavy_atoms"    ,
          "RD_num_arom_rings": "num_atom_rings" ,
          "RD_num_alip_rings": "num_alip_rings" ,
           "RD_num_sat_rings": "num_sat_rings"  ,
           "RD_Stereocenters": "num_stereo"     ,
             "RD_Spiro_atoms": "num_spiro"      ,
                    "RD_LogP": "logp"           ,
                    "RD_TPSA": "tpsa"           ,
                  "RD_SYNTHA": "syntha"         ,
                     "RD_QED": "qed"            ,
                    "RD_LogS": "logs"           ,
            "RD_num_of_PAINS": "num_pain"       ,
             "RD_PAINS_names": "pains_names"    ,
                  "RD_SMILES": "smiles"         
}


pandas_dict = {
             #0:pd.StringDtype(),
             #1:pd.StringDtype(),
             #2:pd.Int64Dtype(),
             #3:pd.Int64Dtype(),
             #4:pd.StringDtype(),
             #5:pd.Float64Dtype(),
             #6:"Int8",
            # 7:"Float64",
             #8:"Int8",
            # 9:"Int8",
            #10:"Int8",
            #11:"Int8",
            #12:"Int8",
            #13:"Int8",
            #14:"Int8",
            #15:"Int8",
           # 16:pd.Float64Dtype(),
           # 17:pd.Float64Dtype(),
           # 18:pd.Float64Dtype(),
           # 19:pd.Float64Dtype(),
           # 20:pd.Float64Dtype(),
           # 21:pd.Int64Dtype(),
           # 22:pd.StringDtype(),
           # 23:pd.StringDtype()
}
