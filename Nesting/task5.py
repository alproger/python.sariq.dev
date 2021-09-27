davlatlar  = {
    'Uzbekistan' : {
        'nomi' : 'Uzbekistan',
        'poytaxti' : 'Toshkent',
        'aholisi' : 35_000_000,
        'puli' : 'so\'m',
        'tili' : 'o\'zbek tili'  },
    'Aqsh':{
        'nomi' : 'Amerika qo\'shma shtatlari',
        'poytaxti' : 'Washington',
        'aholisi' : 560_000_000,
        'puli' : 'do\'llar',
        'tili' : 'amerika ingliz tili'
    },
    'Rossiya' :{
        'nomi' : 'Rossiya Federatsiyasi',
        'poytaxti' : 'Moskava',
        'aholisi' : 350_000_000,
        'puli' : 'Rubl',
        'tili' : 'Rus tili'
    },
    'Hindiston' : {
         'nomi' : 'Hindiston',
        'poytaxti' : 'Dehli',
        'aholisi' : 2_000_000_000,
        'puli' : 'Rubpi',
        'tili' : 'Hind va ingliz tili'
    },
}
 
enter = input('Davlat nomini kiriting : ')

if enter.title() in davlatlar.keys():
    
    info = f'{davlatlar[enter]["nomi"]}ning poytaxti '
    info += f'{davlatlar[enter]["poytaxti"]} '
    info += f'aholisi {davlatlar[enter]["aholisi"]} '
    info += f'kishi pul birligi {davlatlar[enter]["puli"]} '
    print(info)

else :
    print('Bunday davlat haqida bizda malumot yo\'q')


        