import unittest

from mol2obj import utilities as ut


class Test_Utilities_Func(unittest.TestCase):

    def test_is_floatnumber(self):
        tests = [
                (["5.4","3.0000","0.00001"],True),
                (["5","3","0"],False),
                (["5.4","3.0000","0"],False)]
   
        for test,expected in tests:
            with self.subTest(value=test): 
                self.assertEqual(ut.is_floatnumber(test), expected)

    def test_is_intnumber(self):
        tests = [
                (["5.4","3.0000","0.00001"],False),
                (["5","3","0"],True),
                (["5.4","3.0000","0"],False)]

        for test,expected in tests:
            with self.subTest(value=test):
                self.assertEqual(ut.is_intnumber(test), expected) 


if __name__ == '__main__':
    unittest.main(verbosity=2)

