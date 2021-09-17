countries = ['USA', 'UZBEKISTAN', 'UK', 'CANADA', 'SPAIN', 'QATAR', 'UEA', 'SURIA']

# royhatni ekranga chiqarish
print(countries)

#ro'yhat uzunligi
print(len(countries))

#tartiblangan ro'yhat
print(sorted(countries))

#teskari tartiblangan ro'yhat
print(sorted(countries, reverse=True))

#asl ro'yhat
print(countries)

#reverce metodi yordamida teskari tartiblangan ro'yhat
countries.reverse()
print(countries)

#sorted metodi yordamida ro'yhatni tartiblash
countries.sort() # alifbo tartibida
print(countries)

countries.sort(reverse=True) #alifboga teskari tartibda
print(countries) 
