class Auto:
    
    def __init__(self, company, model, color, cost) :
        '''Avtomobil klasining qiymatlari  '''
        
        self.company = company
        self.model = model
        self.color = color
        self.cost = cost
        self.km = 0
    
    def get_info(self):
        '''Avtomobil haqida to'liq malumot qaytaradi'''
        info = f'Avtomobil {self.model} ishlab chiqaruvchi {self.company} narxi {self.cost}$ rangi {self.color} bosgan masofasi {self.km} km'
        return info

    def get_company(self):
        '''Avtomobilni ishlab chiqaruvchi kompaniya nomini qaytaradi'''
        return self.company
    
    def get_model(self):
        '''Avtomobilning modelini qaytaruvchi funksiya'''
        return self.model
    
    def get_color(self):
        '''Avtomobilning rangini qaytaruvchi funksiya'''
        return self.color
    
    def get_cost(self):
        '''Avtomobilning narxini qaytaradi'''
        return self.cost
    
    def get_km(self):
        '''Avtomobilning yurgan masofasini qaytaradi'''
        return self.km

    def update_km(self, new_km):
        '''Avtomobilning yurgan masofasiga yana masofa qoshish uchun funksiya'''
        self.km += new_km
    
    def set_km(self, new_km):
        '''Avtomobilning yurgan masofasini yangilaydigan funksiya'''
        self.km = new_km


    def set_color(self, new_color):
        '''Avtomobilning rangini yangilash uchun funksiya'''
        self.color = new_color
    
    def set_cost(self, new_cost):
        '''Avtomobilning narxini yangilash uchun funksiya'''
        self.cost = new_cost


car1 = Auto('BMW', 'X7', 'qora', 40000)
car2 = Auto('Chevrolet', 'Captiva 4', 'oq', 35000)

car1.update_km(100)
car1.set_cost(21000)
car1.set_color('sariq')
print(car1.get_info())
