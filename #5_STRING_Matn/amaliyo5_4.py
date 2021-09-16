
kocha = input('ko\'cha nomini kiriting : ')
mahalla = input('mahallas nomini kiriting :  ')
tuman = input('tuman nomini kiriting : ')
viloyat = input('viloyat nomini kiriting : ')

# 1-usul
#matn = f'{kocha} ko\'chasi, \n{mahalla} mahllasi, \n{tuman} tumani, \n{viloyat} viloyati'

# 2-usul
#matn = '{} ko\'chasi, \n{} mahallasi, \n{} tuman, \n{} viloyati '.format(kocha,mahalla,tuman,viloyat)

# 3-usul
matn = kocha + ' ko\'chasi, \n' + mahalla + ' mahallasi, \n' + tuman + ' tumani, \n' + viloyat + ' viloyati'

print(matn)