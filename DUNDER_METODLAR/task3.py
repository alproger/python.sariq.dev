from task1_2 import Talaba

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

talaba1 = Talaba('Sarvar', 'Zokirov', 'AA121313123', 1999, 'T.A.T.U')
talaba2 = Talaba('Ali', 'Valiyev', 'AA1423423', 1998, 'FarDU')
talaba3 = Talaba('Bahrom', 'Fozilov', 'AA565656', 1990, 'FarPI')

fan1 = Fan('English lang', 30, 'Behzod Palonchiyev')
fan1.add_student(talaba1, talaba2)
fan1 + talaba3

print(fan1[:])

