import unittest
from functions import evenNumberFunction

class EvenNumbersFunctionTest(unittest.TestCase):
    '''evenNumberFunction ni tekshirish uchun test klasi'''
    
    def test1_evenNumsFunc(self):
        '''evenNumberFunction ni tekshiruvchi metod test1'''
        info = list(range(1,11))
        function_result = evenNumberFunction(info)
        true_result = [2, 4, 6, 8, 10]
        self.assertEquals(function_result, true_result)
    
    def test2_evenNumsFunc(self):
        '''evenNumberFunction ni tekshiruvchi metod test2'''
        info = list(range(0, 21,2))
        function_result = evenNumberFunction(info)
        true_result = info
        self.assertEquals(function_result, true_result)
    
    def test3_evenNumsFunc(self):
        '''evenNumberFunction ni tekshiruvchi metod test3'''
        info = list(range(1, 21, 2))
        function_result = evenNumberFunction(info)
        true_result = []
        self.assertEquals(function_result, true_result)


unittest.main()
