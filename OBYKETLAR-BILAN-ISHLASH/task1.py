class Auto:
    
    def __init__(self, company, model, color, cost) :
        '''Avtomobil klasining qiymatlari  '''
        
        self.company = company
        self.model = model
        self.color = color
        self.cost = cost
        self.km = 0
    
car1 = Auto('BMW', 'X7', 'black', 40000)

print(car1.company)
print(car1.model)
print(car1.color)
print(car1.cost)
print(car1.km)
