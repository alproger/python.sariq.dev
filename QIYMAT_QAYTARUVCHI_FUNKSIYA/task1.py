
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

sarvarboy = malumot('Sarvarbek', 'Zokirxonov', 'Qirgiz tumani', 1441, 'sacasd@fdhgd.com', '+9989000000000')

print(sarvarboy['ism'])
print(sarvarboy['tel'])
print(sarvarboy['yosh'])