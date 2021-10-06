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
    
    #dundee method

    def __repr__(self):
        '''shaxs klasining malumotini qaytaradi '''
        return f'Shaxs : {self.ism} {self.familya}'


    def __call__(self):
        '''shaxs obyektini chaqirganimizda malumot qaytaradi '''
        return f'Shaxs {self.ism} {self.familya} '
    
    #tenglik
    def __eq__(self, person):
        '''shaxslarni solish tirish tengmi metodi x == y'''
        return self.yosh == person.yosh
    
    #kichik
    def __lt__(self, person):
        '''shaxsni boshqa shaxsdan kichik ligini aniqlaydi'''
        return self.yosh < person.yosh

    #kichik yoki teng
    def __le__(self, person):
        '''shaxslarni solish tirish kixhik yoki teng x < y'''
        return self.yosh <= person.yosh
    
    #katta
    def __gt__(self, person):
        '''shaxsni boshqa shaxdan kattaligini aniqlaydi'''
        return self.yosh > person.yosh
    
    # katta yoki teng
    def __de__(self, person):
        '''shaxsni boshqa shaxsdan katta yoki tengligini aniqlaydi '''
        return self.yosh >= person.yosh        

shaxs1 = Shaxs('Sarvar', 'Zokirov', 'AA1212122', 1999)
shaxs2 = Shaxs('Sarvar', 'Zokirov', 'AA1212122', 1999)

print(shaxs1())
print(shaxs2)
print(shaxs1 < shaxs2)
print(shaxs1 > shaxs2)
print(shaxs1 <= shaxs2)
print(shaxs1 >= shaxs2)

