def taqqosla(qiymat1, qiymat2):
    '''Foydalanuvchidan ikkita son olib, ulardan kattasini
       konsolga chiqaruvchi funksiya'''
    
    result = 0
    result = qiymat1 if qiymat1 > qiymat2 else qiymat2
    if qiymat1 == qiymat2 :
        result = 'sonlar teng'
    
    print(result)

print('2 ta son kiriting : ')
son1 = int(input("1-son : "))
son2 = int(input("2-son : "))

taqqosla(son1, son2)
