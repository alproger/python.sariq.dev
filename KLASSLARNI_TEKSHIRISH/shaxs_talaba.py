class Shaxs:
    '''Shaxs klasi shaxsga oid malumotlar bilan ishlash uchun'''
    
    def __init__(self, ism, familya, passport, t_yil):
        '''shaxs klasining hususiyatlari'''
        
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.t_yil = t_yil
        self.yosh = 2021 - int(t_yil)

    def get_info(self):
        '''Shaxsga tegishli hususiyatlarni qaytaradi'''
        info = f'Shaxs {self.ism} {self.familya} passport : {self.passport} {self.t_yil}-yilda tug\'ulgan. {self.yosh} yoshda.'
        return info
    
    def get_fullname(self):
        '''shaxsga tegishli ism va familiyani qaytaradi'''
        return f'{self.ism} {self.familya}'

    def get_passport(self):
        '''shaxsga tegishli passport malumotini qaytaradi'''
        return self.passport
    
    def get_year(self):
        '''shaxsga tegishli yosh malumotini qaytaradi'''
        return self.yosh
    

    


class Talaba(Shaxs):
    '''shaxs klasidan nasl olgan talaba klasi. Bu klass talabalarning malumotlari bilan ishlash uchun'''

    def __init__(self, ism, familya, passport, t_yil, universitet, talabaId, course = 1):
        '''Talaba klasining hususiyatlarini saqlovchi funksiya'''
        super().__init__(ism, familya, passport, t_yil)
        self.unversitet = universitet
        self.talabaId = talabaId
        self.cours = course


    def get_univer(self):
        '''Talaba klasiga tegishli obyektning universitet malumotini qaytaradi'''
        return self.unversitet

    def get_studentId(self):
        '''talaba klasiga tegishli obyektning studentId malumotini qaytaradi'''
        return self.talabaId
    
    def get_cours(self):
        '''talabaning kursni qaytaradi'''
        return self.cours
    
    def add_cours(self):
        '''talabaning kursini 1 ta kursga oshiradi'''
        self.cours += 1
        return self.cours
        


    