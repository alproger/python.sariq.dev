
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
    


class Talaba(Shaxs):
    '''shaxs klasidan nasl olgan talaba klasi. Bu klass talabalarning malumotlari bilan ishlash uchun'''

    def __init__(self, ism, familya, passport, t_yil, universitet, talabaId):
        '''Talaba klasining hususiyatlarini saqlovchi funksiya'''
        super().__init__(ism, familya, passport, t_yil)
        self.unversitet = universitet
        self.talabaId = talabaId
        self.fanlar = []

    def get_univer(self):
        '''Talaba klasiga tegishli obyektning universitet malumotini qaytaradi'''
        return self.unversitet

    def get_studentId(self):
        '''talaba klasiga tegishli obyektning studentId malumotini qaytaradi'''
        return self.talabaId
    
    def fanga_yozil(self, fan):
        '''talaba klasiga tegishli obyektga fan yozuchi funksiya'''
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        '''talabaga tegishli fanni ochirib tashlovchi funksiya'''
        
        if fan in self.fanlar:
            self.fanlar.remove(fan)

        else :
            print('Siz bu fanga yozilmagansiz')



class Fan:
    ''''Fan klasi turli xil fanga oid malumotlar bilan ishlash uchun'''
    
    def __init__(self, nomi, soati, kafedrasi, ustozi):
        '''fan klasiga tegishli qiymatlarni saqlovchi funksiya'''
        self.nomi = nomi
        self.soati = soati
        self.kafedrasi = kafedrasi
        self.ustozi = ustozi
    
    def get_info(self):
        '''Fan klasi obyekti haqida to'liq malumot qaytaruvchi funksiya'''
        info = f'{self.nomi} fani {self.kafedrasi} kafedrasiga qarashli {self.soati} soatdan iborat o\'qituvchisi {self.ustozi}'
        return info
    
    def get_subj(self):
        '''Fan nomini qaytaradi'''
        return self.nomi
    
    def get_teacher(self):
        '''Fan o'qituvchisini qaytaradi'''
        return self.ustozi
    
    def get_hour(self):
        '''Fanning davomiylik soatini qaytaradi'''
        return self.soati


fan1 = Fan('Dasturlash asoslari', 30, 'Dasturiy injinering', 'Anvar Nazrullayev')
fan2 = Fan('Fulstack Python', 100, 'Dasturiy injinering', 'Jahongir Rahmonov')
fan3 = Fan('Oliy Matematika', 60, 'Aniq fanlar', 'Yodgor Yusupov')

talaba1 = Talaba('Valijon', 'Valiyev', 'AA4545505', 1999, 'T.A.T.U', 'N1230003')
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)

talaba1.remove_fan(fan2)

print([fan.get_subj() for fan in talaba1.fanlar ])
