def aylana(r):
    """Foydalanuvchidan aylana radiusini qabul qilib aylananing boshqa qiymatlarini
       aniqlaydigan funksiya diametri, uzunligi va yuzasini aniqlaydi """
    aylanaa = {
        'r' : r,
        'd' : r * 2,
        'l' : 3.14 * 2 * r,
        's' : 3.14 * (r ** 2)
                              }

    return aylanaa

malumot = aylana(10)
print(f'aylana diametri : {malumot["d"]}')
print(f'aylana uzunligi : {malumot["l"]}')
print(f'aylana yuzasi : {malumot["s"]}')    