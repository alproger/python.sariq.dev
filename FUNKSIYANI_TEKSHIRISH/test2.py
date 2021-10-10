import unittest
from functions import titleFunction

class TitleFunctionTest(unittest.TestCase):
    '''titleFunction funksiyasini tekshiruvchi klass'''

    def test_title(self):
        '''titleFunction funksiyasini tekshiruvchi metod'''
        info = ['salom', 'assalom', 'taom', 'yaxshi', 'yomon']
        function_result = titleFunction(info)
        true_result = ['Salom', 'Assalom', 'Taom', 'Yaxshi', 'Yomon']
        self.assertEquals(function_result, true_result)

unittest.main()