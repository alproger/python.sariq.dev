from myRandom import Lotoreya , OmadliRaqam

foydalanuvchilar = ['Alijon', 'Valijon', 'Akmal', 'Ahror', 'Diyor', 'Sarvar']

#lotareya o'yinida g'olibni aniqlash uchun kichik dastur 
golib = Lotoreya(foydalanuvchilar)
print(golib)

#omadli raqam chiqsa pul yutasiz
raqamlar = list(range(1, 101, 1))
omadli = OmadliRaqam(raqamlar)
print(omadli)


