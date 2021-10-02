class AutoSalon:
    def __init__(self, nomi, manzili):
        '''AutoSalon klasining qiymatlari'''
        self.nomi = nomi
        self.mazili = manzili
        self.avtolar_soni = 0
        self.avtolar = []

salon1 = AutoSalon('Uzcars', 'Fargona viloyati, Al-Fargoniy ko\'chasi 130-uy')
print(salon1.mazili)
