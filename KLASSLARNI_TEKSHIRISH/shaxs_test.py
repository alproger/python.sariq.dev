from logging import info
import unittest
from shaxs_talaba import Shaxs

class ShaxsTest(unittest.TestCase):
    '''Shaxs klasini tekshiramiz'''

    def setUp(self):
        '''test qilish uchun qiymatlarni saqlash'''
        self.ism = 'Anvar'
        self.familya = 'Nazrullayev'
        self.passport = 'AA121212'
        self.t_yil = 1988
        self.yosh = 2021 - int(self.t_yil)
        self.shaxs = Shaxs(self.ism, self.familya, self.passport, self.t_yil)


    def test_values(self):
        '''Shaxs klasining qiymatlarini tekshiramiz'''
        
        # qiymatlari mavjudligini tekshiramiz
        self.assertIsNotNone(self.shaxs.ism)
        self.assertIsNotNone(self.shaxs.familya)
        self.assertIsNotNone(self.shaxs.passport)
        self.assertIsNotNone(self.shaxs.t_yil)
        self.assertIsNotNone(self.shaxs.yosh)

        # qiymatlari to'g'riligini tekshiramiz
        self.assertEqual(self.ism, self.shaxs.ism)
        self.assertEqual(self.familya, self.shaxs.familya)
        self.assertEqual(self.passport, self.shaxs.passport)
        self.assertEqual(self.t_yil, self.shaxs.t_yil)
        self.assertEqual(self.yosh, self.shaxs.yosh)
    
    def test_methods(self):
        '''Shaxs klasining metodlarini tekshiramiz'''
        self.assertEqual(self.shaxs.get_fullname(), 'Anvar Nazrullayev')
        self.assertEqual(self.shaxs.get_passport(), self.passport)
        self.assertEqual(self.shaxs.get_year(), self.yosh)
        inf = f'Shaxs {self.ism} {self.familya} passport : {self.passport} {self.t_yil}-yilda tug\'ulgan. {self.yosh} yoshda.'
        self.assertEqual(self.shaxs.get_info(), inf)
    




unittest.main()



        