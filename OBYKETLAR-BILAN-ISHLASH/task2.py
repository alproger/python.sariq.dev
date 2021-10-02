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
        info = f'Avtomobil {self.model} ishlab chiqaruvchi {self.company} narxi {self.cost} rangi {self.color} bosgan masofasi {self.km}'
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

car1 = Auto('BMW', 'X7', 'qora', 40000)
car2 = Auto('Chevrolet', 'Captiva 4', 'oq', 35000)

print(car1.get_company())
print(car2.get_company())
