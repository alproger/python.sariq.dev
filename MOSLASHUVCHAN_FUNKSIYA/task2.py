def malumotnoma(ism, familiya, **malumotlar) :
    '''malumotlarni qbul qilib lug'at ko'rinishda qaytaruvchi funksiya'''
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya

    return malumotlar

malumotlarim = malumotnoma('Jon', 'Tomson', yoshi = 23, tyil=1998, davlati = 'AQSH', kasbi = 'Dasturchi')
print(malumotlarim)