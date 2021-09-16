sonlar = [1, -2, 3.0, 4.1, 5]

#arifmetik amallar
sonlar[0] = sonlar[0] + 2
sonlar[1] = sonlar[0] + sonlar[2]
sonlar[2] = sonlar[1] * sonlar[3]
sonlar[3] = sonlar[3] - sonlar[4]
sonlar[4] = sum(sonlar)
print(sonlar)

sonlar[1] = sonlar[0]
sonlar.insert(2,10)
print(sonlar)