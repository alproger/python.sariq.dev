from bironta_funksiya import summator, darajator, kopaytrator

#sonlarning yeg'indisini hisoblaydi
summa = summator(1,2,3,4,5,6,7,8,9)

#sonlaring ko'paytmasini hisoblaydi
kopaytma = kopaytrator(1,2,3,4,5,6,7,8,9)

#sonlarning darajasini chiqaradi
sonlar  = list(range(1, 10))
darajalar = darajator(sonlar, daraja= 2)

print(summa)
print(kopaytma)
print(darajalar)
