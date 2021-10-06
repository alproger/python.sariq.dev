from task1_1 import Shaxs


class Talaba(Shaxs):
    __talabalar_soni = 0
    
    '''shaxs klasidan nasl olgan talaba klasi. Bu klass talabalarning malumotlari bilan ishlash uchun'''
    
    def __init__(self, ism, familya, passport, t_yil, universitet, talabaID):
        '''Talaba klasining hususiyatlarini saqlovchi funksiya'''
        super().__init__(ism, familya, passport, t_yil)
        self.unversitet = universitet
        self.__talabaId = talabaID
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
        return f'{self.unversitet}ning {self.__kurs}-bosqich talabasi {self.ism} {self.familya}'
    
    def __repr__(self):
        '''Talaba klasi obyekti haqida qisqa malumot qaytaradi'''
        return  f'Talaba : {self.ism} {self.familya}'

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





class Fan:
    '''Fan klasi turli fanga doir obyektlar yaratish uchun'''
    
    def __init__(self, fanNomi, vaqti, ustozi) :
        '''fan klasining qiymatlarini saqlovchi funksiya'''
        self.fanNomi = fanNomi
        self.vaqti = vaqti
        self.ustozi = ustozi
        self.talabalar = []

    def add_student(self, *args):
        '''Fanga 1 va undan ko'p talabalarni yozuvchi funksiya'''
        [self.talabalar.append(talaba) for talaba in args]
    
    def __getitem__(self, index):
        '''fanga yozilgan talabalarning indeksi boyicha chaqirish'''
        return self.talabalar[index]
    
    def __setitem__(self, index , otherStudent):
        '''fanga yozilgan talabani o'rniga boshqa talabani qo'yish'''
        self.talabalar[index] = otherStudent

    def __add__(self, other):
        '''Fanga + orqali talaba qo'shish metodi qoshilayotgan  
        talaba Talaba klasiga tegishli bo'lishi kerak'''
        if isinstance(other, Talaba):
            self.talabalar.append(other)

    def __sub__(self, talaba):
        '''fandan talabani id orqali topib o'chirib tashlovchi metod'''
        
        for student in self.talabalar:
            student_id = student.get_studentId()
            passport = student.get_passport()
            
            if student_id ==  talaba.get_studentId()  or passport == talaba.get_passport() :
                self.talabalar.remove(talaba)

            else :
                print('Bunday talaba mavjud emas')

talaba1 = Talaba('Sarvar', 'Zokirov', 'AA121313123', 1999, 'T.A.T.U', 'T0001')
talaba2 = Talaba('Ali', 'Valiyev', 'AA1423423', 1998, 'FarDU', 'T0002')
talaba3 = Talaba('Bahrom', 'Fozilov', 'AA565656', 1990, 'FarPI', 'T0003')

fan1 = Fan('English lang', 30, 'Behzod Palonchiyev')
fan1.add_student(talaba1, talaba2, talaba3)
print(fan1[:])

fan1 - talaba1
print(fan1[:])

