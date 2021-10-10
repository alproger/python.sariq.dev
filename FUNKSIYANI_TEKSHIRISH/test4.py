import unittest
from functions import get_fib

class IsFibonachiNumsTest(unittest.TestCase):
    '''isFibonacciNums fuksiyasini tekshiruvchi klass'''

    def test1_getFib(self): 
        info = 1
        functionResult = get_fib(info)
        true_result  = True
        self.assertEquals(functionResult, true_result)

    def test2_getFib(self): 
        info = 9
        functionResult = get_fib(info)
        true_result  = False
        self.assertEquals(functionResult, true_result)

    def test3_getFib(self): 
        info = 7
        functionResult = get_fib(info)
        true_result  = False
        self.assertEquals(functionResult, true_result)



    
unittest.main()