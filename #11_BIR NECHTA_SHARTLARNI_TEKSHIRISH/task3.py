print('2 ta son kiriting ')
son1 = int(input('1-son : '))
son2 = int(input('2-son : '))

result = ''
if son1 == son2 :
    result = 'Sonlar o\'zaro teng'

elif son1 > son2 : 
    result = '1-son katta'

else :
    result = '2-son katta'

print(result)