from uuid import uuid4
from task1_1 import Shaxs


class Talaba(Shaxs):
    __talabalar_soni = 0
    
    '''shaxs klasidan nasl olgan talaba klasi. Bu klass talabalarning malumotlari bilan ishlash uchun'''
    
    def __init__(self, ism, familya, passport, t_yil, universitet):
        '''Talaba klasining hususiyatlarini saqlovchi funksiya'''
        super().__init__(ism, familya, passport, t_yil)
        self.unversitet = universitet
        self.__talabaId = uuid4()
        self.__kurs = 1
        Talaba.__talabalar_soni += 1


    def get_univer(self):
        '''Talaba klasiga tegishli obyektning universitet malumotini qaytaradi'''
        return self.unversitet

    def get_studentId(self):
        '''talaba klasiga tegishli obyektning studentId malumotini qaytaradi'''
        return self.__talabaId
    
    def get_kurs(self):
        '''talabaning o'qiyotgan kursini qaytaradi'''
        return self.__kurs

    def update_kurs(self):
        '''talabaning kursini yangilash bunda faqa 1 ta kurs yuqorilaydi'''
        self.__kurs += 1

    def __call__(self):
        '''talaba klasiga tegishli obyektni chaqirganda ishga tushadi'''
        return f'Talaba : {self.ism} {self.familya}'
    
    def __repr__(self):
        '''Talaba klasi obyekti haqida qisqa malumot qaytaradi'''
        return f'{self.unversitet}ning {self.__kurs}-bosqich talabasi {self.ism} {self.familya}'

    @classmethod
    def get_talabalar_soni(cls):
        '''class metodi bu metod umumiy talaba clasidan yaratilgan obyektlar sonini qaytaradi'''
        return Talaba.__talabalar_soni

    def __eq__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (==)'''
        return self.__kurs == other.__kurs
    
    def __lt__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (<)'''
        return self.__kurs < other.__kurs
    
    def __gt__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (>)'''
        return self.__kurs > other.__kurs
    
    def __le__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (<=)'''
        return self.__kurs <= other.__kurs
    
    def __ge__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (>=)'''
        return self.__kurs >= other.__kurs
    
    def __ne__(self, other):
        '''talabalarni bosqichi bo'yicha taqqoslash (!=)'''
        return self.__kurs != other.__kurs





talaba1 = Talaba('Sarvar', 'Zokirov', 'AA121313123', 1999, 'T.A.T.U')
talaba1.update_kurs()

talaba2 = Talaba('Ali', 'Valiyev', 'AA1423423', 1998, 'FarDU')

print(talaba1)
print(talaba2())

print(talaba1 == talaba2)
print(talaba1 > talaba2)
print(talaba1 < talaba2)
print(talaba1 >= talaba2)
print(talaba1 <= talaba2)
print(talaba1 != talaba2)