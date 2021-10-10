import unittest
from shaxs_talaba import Talaba

class TalabaTest(unittest.TestCase):
    '''Talaba klasini tekshiramiz'''

    def setUp(self):
        '''test qilish uchun qiymatlarni saqlash'''
        self.ism = 'Anvar'
        self.familya = 'Nazrullayev'
        self.passport = 'AA121212'
        self.t_yil = 1988
        self.yosh = 2021 - int(self.t_yil)
        self.kurs = 3
        self.univer = 'TATU'
        self.studentId = 'N000001'
        self.talaba = Talaba(self.ism, self.familya, self.passport, self.t_yil, self.univer, self.studentId)
        self.talaba2 = Talaba(self.ism, self.familya, self.passport, self.t_yil, self.univer, self.studentId, self.kurs)

    def test_values(self):
        '''Talaba klasining qiymatlarini tekshiramiz'''
        
        # qiymatlari mavjudligini tekshiramiz
        self.assertIsNotNone(self.talaba.ism)
        self.assertIsNotNone(self.talaba.familya)
        self.assertIsNotNone(self.talaba.passport)
        self.assertIsNotNone(self.talaba.t_yil)
        self.assertIsNotNone(self.talaba.yosh)
        self.assertIsNotNone(self.talaba.unversitet)
        self.assertIsNotNone(self.talaba.talabaId)

        # qiymatlari to'g'riligini tekshiramiz
        self.assertEqual(self.ism, self.talaba.ism)
        self.assertEqual(self.familya, self.talaba.familya)
        self.assertEqual(self.passport, self.talaba.passport)
        self.assertEqual(self.t_yil, self.talaba.t_yil)
        self.assertEqual(self.yosh, self.talaba.yosh)
        self.assertEqual(self.univer, self.talaba.unversitet)
        self.assertEqual(self.studentId, self.talaba.talabaId)
        self.assertEqual(self.talaba.cours, 1)
        self.assertEqual(self.talaba2.cours, self.kurs)

    def test_methods(self):
        '''Talaba klasining metodlarini tekshiramiz'''
        self.assertEqual(self.talaba.get_fullname(), 'Anvar Nazrullayev')
        self.assertEqual(self.talaba.get_passport(), self.passport)
        self.assertEqual(self.talaba.get_year(), self.yosh)
        inf = f'Shaxs {self.ism} {self.familya} passport : {self.passport} {self.t_yil}-yilda tug\'ulgan. {self.yosh} yoshda.'
        self.assertEqual(self.talaba.get_info(), inf)
        self.assertEqual(self.talaba.get_univer(), self.univer)
        self.assertEqual(self.talaba.get_cours(), 1)
        self.assertEqual(self.talaba2.get_cours(), self.kurs)
        self.assertEqual(self.talaba.get_studentId(), self.studentId)
        self.assertEqual(self.talaba.add_cours(), 2)
        self.assertEqual(self.talaba2.add_cours(), 4)


unittest.main()