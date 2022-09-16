import unittest

from mol2obj import utilities as ut


class Test_Utilities_Func(unittest.TestCase):

    def test_is_floatnumber(self):
        tests = [
                (["5.4","3.0000","0.00001"],True),
                (["5","3","0"],False),
                (["5.4","3.0000","0"],False), 
                ([5.4],False)
                ]
                
   
        for test,expected in tests:
            with self.subTest(value=test): 
                self.assertEqual(ut.is_floatnumber(test), expected)

    def test_is_intnumber(self):
        tests = [
                (["5.4","3.0000","0.00001"],False),
                (["5","3","0"],True),
                (["5.4","3.0000","0"],False),
                ([5.4],False),
                ("single_string",False)
                ]

        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.is_intnumber(test), expected) 
    def test_if_atom(self):
        tests = [
                ("      1 O1         -0.0173    1.4248    0.0099 O.3     1  <0>        -0.5700",True),
                ("       O1         -0.0173    1.4248    0.0099 O.3     1  <0>        -0.5700",False),
                ("                -0.0173    1.4248    0.0099 O.3     1  <0>        -0.5700",False),
                (1,False),
                ("single_string",False)
                ]

        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.if_atom(test), expected)

    def test_if_bond(self):
        tests = [
                ("     1     1     2    1",True),
                ("     1     1     2    ar",True),
                ("     1.1   1     2    1",False),
                ("     -1     1     2    1",False),
                ("     1   -1     2    1",False), 
                (1,False),
                ("single_string",False)
                
                ]

        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.if_bond(test), expected) 

    def test_if_header(self):
        tests = [
                ("##########                     HBond_Acceptors:                   3",True),
                ("##########          HBond_Acceptors:   3",True),
                ("     1     1     2    ar",False),
                ("     1.1   1     2    1",False),
                ("     -1     1     2    1",False),
                ("     1   -1     2    1",False),
                (1,False),
                ("single_string",False)

                ]

        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.if_header(test), expected)

    def test_calc_num_mol(self):
        with open("../tests_files/example.mol2", "r") as mol2:
            readlines = mol2.readlines()
        tests= [
               (readlines,2)
               ]
        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.calc_num_mol(test), expected) 


    def test_get_headers_names(self):
        with open("../tests_files/example.mol2", "r") as mol2:
            readlines = mol2.readlines()            

        tests= [
               (readlines,[["Name:","Molecular_Weight:","DOCK_Rotatable_Bonds:","Formal_Charge:", 
                           "HBond_Acceptors:","HBond_Donors:","Heavy_Atoms:","RD_num_arom_rings:",  
                           "RD_num_alip_rings:","RD_num_sat_rings:","RD_Stereocenters:","RD_Spiro_atoms:",
                           "RD_LogP:","RD_TPSA:","RD_SYNTHA:","RD_QED:","RD_LogS:","RD_num_of_PAINS:","RD_PAINS_names:","RD_SMILES:"],
                           ["Name:","Molecular_Weight:","DOCK_Rotatable_Bonds:","Formal_Charge:", 
                           "HBond_Acceptors:","HBond_Donors:","Heavy_Atoms:","RD_num_arom_rings:",
                           "RD_num_alip_rings:","RD_num_sat_rings:","RD_Stereocenters:","RD_Spiro_atoms:",
                           "RD_LogP:","RD_TPSA:","RD_SYNTHA:","RD_QED:","RD_LogS:","RD_num_of_PAINS:","RD_PAINS_names:","RD_SMILES:"]
                           ]),
               #(readlines,[["Name:","Molecular_Weight:","DOCK_Rotatable_Bonds:","Formal_Charge:",
               #            "HBond_Acceptors:","HBond_Donors:","Heavy_Atoms:","RD_num_arom_rings:",
               #            "RD_num_alip_rings:","RD_num_sat_rings:","RD_Stereocenters:","RD_Spiro_atoms:",
               #            "RD_LogP:","RD_TPSA:","RD_SYNTHA:","RD_QED:","RD_LogS:","RD_num_of_PAINS:","RD_PAINS_names:","RD_SMILES:"],
               #            ["Name:","Molecular_Weight:","DOCK_Rotatable_Bonds:","Formal_Charge:",
               #            "HBond_Acceptors:","HBond_Donors:","Heavy_Atoms:","RD_num_arom_rings:",
               #            "RD_num_alip_rings:","RD_num_sat_rings:","RD_Stereocenters:","RD_Spiro_atoms:",
               #            "RD_LogP:","RD_TPSA:","RD_SYNTHA:","RD_QED:","RD_LogS:","RD_num_of_PAINS:","RD_PAINS_names:","RD_SMILES:"]
               #            ]),
               ]
        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.get_headers_names(test), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)

