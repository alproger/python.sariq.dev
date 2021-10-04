
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
        return ''.join(self.ism, self.familya)

    def get_passport(self):
        '''shaxsga tegishli passport malumotini qaytaradi'''
        return self.passport


class Foydalanuvchi(Shaxs):
    '''sayt foydalanuvchilarini malumotlari qayta ishlash uchun klass'''
    def __init__(self, ism, familya, passport, t_yil, login, parol):
        super().__init__(ism, familya, passport, t_yil)
        self.login = login
        self.parol = parol
    
    def get_info(self):
        '''foydalanuvchi klasiga tegishli obyektning malumotini qaytaruvchi funksiya'''
        info = f'Foydalanuvchi {self.ism} {self.familya} {self.t_yil}-yilda tug\'ulgan '
        info += f'passporti {self.passport}, logini : {self.login}, paroli : {self.parol} '
        return info    

    def get_login(self):
        '''foydalanauvchining loginini qaytaradi'''
        return self.login
    
    def get_parol(self):
        '''foydalanuvchining parolini qaytaradi'''
        return self.parol


class Admin(Foydalanuvchi):
    '''Sayt admini malumotlari bilan ishlovchi klas'''
    def __init__(self, ism, familya, passport, t_yil, login, parol, kalit):
        super().__init__(ism, familya, passport, t_yil, login, parol)
        self.kalit = kalit

