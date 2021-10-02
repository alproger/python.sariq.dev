from task3 import Auto

class AutoSalon:
    def __init__(self, nomi, manzili):
        '''AutoSalon klasining qiymatlari'''
        self.nomi = nomi
        self.mazili = manzili
        self.avtolar_soni = 0
        self.avtolar = []

    def add_auto(self, new_auto):
        '''Salonga avtombil yozish uchun funksiya'''
        self.avtolar.append(new_auto)
        self.avtolar_soni += 1
    
    def get_autos(self):
        '''salondagi autolar haqida malumot beradi'''
        return [auto_nomi.company() for auto_nomi in self.avtolar]

    def get_auto_info(self):
        '''salondagi avtolar haqida malumot qaytaradi'''
        return [auto_info.get_info() for auto_info in self.avtolar]
    
    def get_auto_count(self):
        '''Salondagi avtolar sonini qaytaradi'''
        return self.avtolar_soni


car1 = Auto('BMW', 'X7', 'qora', 200000)
car2 = Auto('Ferrari', 'GT133', 'qizil', 100000)

salon1 = AutoSalon('SuperCars', 'Tashkent')
salon1.add_auto(car1)
salon1.add_auto(car2)

print(salon1.get_auto_info())
print(salon1.get_auto_count())