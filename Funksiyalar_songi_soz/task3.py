#3.1 sonlardan iborat ro'yhat elementlaridan faqat 2,3,4,5 bo'linadiganlarini aniqlaydigan funksiyalar

sonlar = list(range(1,51))

# 2 bo'linadigan sonlar
ikki = list(filter(lambda son : son % 2 == 0, sonlar))
#print(ikki)

# 3 bo'linadigan sonlar
uch = list(filter(lambda son : son % 3 == 0, sonlar))
#print(uch)

# 4 bo'linadigan sonlar
tort = list(filter(lambda son : son % 4 == 0, sonlar))
#print(tort)

# 5 bo'linadigan sonlar
besh = list(filter(lambda son : son % 5 == 0, sonlar))
#print(besh)


#3.2 matndan iborat ro'yhat elementlarini hammasi katta harf bilab boshlanganlarini aniqlaydigan funksiya

royhat = ['Python', 'c#', 'Ruby', 'java', 'c++', 'Go', 'css', 'Javascript']

kattaharf =  list(filter(lambda matn : matn == matn.title(), royhat))
print(kattaharf)

