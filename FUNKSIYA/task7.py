def aniqlovchi(qiymat):
    '''Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
       sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya '''
    
    for i in range(2,11):
        if qiymat % i == 0 :
            natija = '{} soni {} ga qoldiqsiz bo\'linadi !'.format(qiymat, i)
            print(natija)

aniqlovchi(210)