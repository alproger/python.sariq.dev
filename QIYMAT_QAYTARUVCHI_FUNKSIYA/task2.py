
def malumot(ism, familya, manzil, tyil, email, tel = None):
    '''Kiritilgan malumotlarni lugat korinishida qaytaruvchi funksiya'''

    malumotlar = {
        'ism'     : ism,
        'falimya' : familya,
        'manzil'  : manzil,
        'tyil'    : tyil,
        'yosh'    : 2021 - int(tyil),
        'email'   : email    }

    if tel :
        malumotlar['tel'] = tel
    
    return malumotlar


mijozlar = []

print('Mijozlar ro\'yhatini tuzamiz malumot kiriting')
while True :
    print('mijoz haqida malumot kiriting ')
    ism = input('ismi : ')
    familya = input('familyasi : ')
    manzil = input('manzili : ')
    tyil = int(input('tugulgan yili : '))
    email = input('email manzili : ')
    tel = input('telefon raqami : ')
    mijoz = malumot(ism, familya, manzil, tyil, email, tel)
    mijozlar.append(mijoz)
    savol = input('yana mijoz qoshasizmi (yes/no) : ')

    if savol == 'no' :
        break

for mijoz in mijozlar:
    print(mijoz)