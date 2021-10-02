from task3 import Auto
from task6 import AutoSalon

car1 = Auto('BMW', 'X7', 'qora', 200000)
car2 = Auto('Ferrari', 'GT133', 'qizil', 100000)

salon1 = AutoSalon('SuperCars', 'Tashkent')
salon1.add_auto(car1)
salon1.add_auto(car2)

'''
print('salon1 obyeksiting metodlari va xususiyatlari')
for direct in dir(salon1):
    print(direct)
'''
'''
print('car1 obyeksiting xususiyatlari')
print(car1.__dict__)
'''
'''
print('Avto klasining metod va hususiyatlari')
for dirs in dir(Auto):
    print(dirs)
'''
''''
print([dirInt for dirInt in dir(int)], '\n')
'''
''''
for dirStr in dir(str):
    print(dirStr)
'''
