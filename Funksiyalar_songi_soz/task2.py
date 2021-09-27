#2.1 ro'yhat elementlarini darajasini oshiruvchi funksiya
daraja = 3
royhat = list(range(1,11))
daraja_oshir = list(map(lambda son : son ** daraja, royhat))
#print(daraja_oshir)


#2.2 ro'yhatdagi matnli elementlarn uchun title(), upper(), lower() va boshqa metodlarni qo'llash
matnlar = ['c#', 'python', 'java','c++', 'go', 'javascript', 'ruby']

#title()
title_adder = list(map(lambda matn : matn.title(), matnlar))
#print(title_adder)

#upper()
upper_adder = list(map(lambda matn : matn.upper(), matnlar))
#print(upper_adder)

#lower()
lower_adder = list(map(lambda matn : matn.lower(), matnlar))
#print(lower_adder)

