
kocha = input('ko\'cha nomini kiriting : ')
mahalla = input('mahallas nomini kiriting :  ')
tuman = input('tuman nomini kiriting : ')
viloyat = input('viloyat nomini kiriting : ')

# 1-usul
#matn = f'{kocha} ko\'chasi, {mahalla} mahllasi, {tuman} tumani, {viloyat} viloyati'

# 2-usul
matn = '{} ko\'chasi, {} mahallasi, {} tuman, {} viloyati '.format(kocha,mahalla,tuman,viloyat)

# 3-usul
#matn = kocha + ' ko\'chasi, ' + mahalla + ' mahallasi, ' + tuman + ' tumani, ' + viloyat + ' viloyati'

print(matn)