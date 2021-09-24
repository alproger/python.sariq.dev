def tyil_hisobla(ism, yil):
    '''Foydalanuvchi ismi va yoshini kiritsa tug'ulgan 
       yilini hisoblab beruvchi funksiya '''
    
    tyil = 2021 - int(yil)
    result = f"{ism} {tyil}-yilda tug'ulgansiz "

    print(result)

ism = input('ismingizni kiriting : ')
yosh = input(f'{ism} yoshingizni kiriting : ')

tyil_hisobla(ism, yosh)
tyil_hisobla()
