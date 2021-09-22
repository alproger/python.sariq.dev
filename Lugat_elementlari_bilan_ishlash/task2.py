counties = {
    
    'USA'        : 'Vashington',
    'Russia'     : 'Moscow',
    'Uzbekistan' : 'Tashkent',
    'UK'         : 'London',
    'Kazakhstan' : 'Astana',
    'Tajikhstan' : 'Dushanbe',
    'Gernamy'    : 'Berlin',
    'Italy'      : 'Rome',
    'France'     : 'Parij',
    'Palastina'  : 'Quddus'

}

for key in sorted(counties.keys()):
    for value in sorted(counties.values()):
        print('Worl countries    |  Capitals   ')
        print(f'{key} | {value} ')
