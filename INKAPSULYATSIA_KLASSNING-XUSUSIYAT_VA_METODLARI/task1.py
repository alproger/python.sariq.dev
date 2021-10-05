from uuid import uuid4

class Shaxs:
    '''Shaxs klasi shaxsga oid malumotlar bilan ishlash uchun'''
    __shaxslar_soni = 0
    def __init__(self, ism, familya, passport, t_yil):
        '''shaxs klasining hususiyatlari'''
        
        self.ism = ism
        self.familya = familya
        self.__passport = passport
        self.t_yil = t_yil
        self.yosh = 2021 - int(t_yil)
        self.__shaxsID = uuid4() 
        Shaxs.__shaxslar_soni += 1


    def get_info(self):
        '''Shaxsga tegishli hususiyatlarni qaytaradi'''
        info = f'Shaxs {self.ism} {self.familya} passport : {self.passport} {self.t_yil}-yilda tug\'ulgan. {self.yosh} yoshda.'
        return info
    
    def get_fullname(self):
        '''shaxsga tegishli ism va familiyani qaytaradi'''
        return f'{self.ism} {self.familya}'

    def get_passport(self):
        '''shaxsga tegishli passport malumotini qaytaradi'''
        return self.__passport
    
    def get_shaxsId(self):
        '''shaxsning id raqamini qaytaradi'''
        return self.__shaxsID
    
    @classmethod
    def get_shaxslar_soni(cls):
        '''shaxs klasidan yasalgan obyektlar sonini qaytaradi'''
        return Shaxs.__shaxslar_soni
    


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

    
    @classmethod
    def get_talabalar_soni(cls):
        '''class metodi bu metod umumiy talaba clasidan yaratilgan obyektlar sonini qaytaradi'''
        return Talaba.__talabalar_soni

shaxs1 = Shaxs('Vali', 'Aliyev', 'AA1212234', 1998)
talaba1 = Talaba('Alijon', 'valiyev', 'AA123454', 1998, 'Tatu')

print(shaxs1.get_shaxsId())
print(talaba1.get_shaxsId())
print(talaba1.get_studentId())

