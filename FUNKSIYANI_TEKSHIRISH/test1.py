import unittest
from functions import maksimum

class MaksTest(unittest.TestCase):
    '''maksimum funksiyasini tekshiruvchi klass'''
    
    def test1_maks(self):
        '''maksimum funksiyasini tekshirish test1'''
        func_result = maksimum(1, 2, 3)
        true_result = 3
        self.assertEqual(func_result, true_result)
    
    def test2_maks(self):
        '''maksimum funksiyasini tekshirish test3'''
        func_result = maksimum(1, 3, 2)
        true_result = 3
        self.assertEqual(func_result, true_result)
    
    def test3_maks(self):
        '''maksimum funksiyasini tekshirish test3'''
        func_result = maksimum(3, 2, 1)
        true_result = 3
        self.assertEqual(func_result, true_result)

unittest.main()