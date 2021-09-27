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

for davlat in davlatlar.keys() :  
        info = f'{davlatlar[davlat]["nomi"]}ning poytaxti '
        info += f'{davlatlar[davlat]["poytaxti"]} '
        info += f'aholisi {davlatlar[davlat]["aholisi"]} '
        info += f'kishi pul birligi {davlatlar[davlat]["puli"]} '
        print(info)
        