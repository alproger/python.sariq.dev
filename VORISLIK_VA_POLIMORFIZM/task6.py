
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
    


class Professor(Shaxs):
    '''Ptofessor haqidagi malumotlar bilan ishlash uchun klass'''
    def __init__(self, ism, familya, passport, t_yil, fani, talim_manzili, shogirdlari_soni, kitoblari):
        super().__init__(ism, familya, passport, t_yil)
        self.fani = fani
        self.talim_manzili = talim_manzili
        self.shogirdlari_soni = shogirdlari_soni
        self.kitoblari = kitoblari
 
    def get_fani(self):
        '''professorning fani nomini qaytaradi'''
        return self.fani
    
    def get_talimMazili(self):
        '''professorning talim berish manzilini qaytaradi'''
        return self.talim_manzili
    
    def get_kitoblari(self):
        '''professor yozgan kitoblar nomini qaytaradi'''
        return self.kitoblari
    
    def get_shogirdlariSoni(self):
        '''professor o'qitgan shogirdlari sonini qaratadi'''
        return self.shogirdlari_soni

class Foydalanuvchi(Shaxs):
    '''sayt foydalanuvchilarini malumotlari qayta ishlash uchun klass'''
    def __init__(self, ism, familya, passport, t_yil, login, parol):
        super().__init__(ism, familya, passport, t_yil)
        self.login = login
        self.parol = parol
    
    def get_login(self):
        '''foydalanauvchining loginini qaytaradi'''
        return self.login
    
    def get_parol(self):
        '''foydalanuvchining parolini qaytaradi'''
        return self.parol


ism = 'Anvar'
familya = 'Nazrullayev'
passport = 'AA131434'
tyil = 1985

professor1 = Professor(ism, familya, passport, tyil, 'Python Dasturlash', 'I.T Unoversitedi', 100000, 'Python')
print(professor1.get_info())

foydalanuvchi1 = Foydalanuvchi(ism, familya, passport, tyil, 'ababab', '1234')
print(foydalanuvchi1.get_info())
