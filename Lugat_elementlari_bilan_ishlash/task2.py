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
print('World countries  |   Capitals   ')
for key, value in  zip(sorted(counties.keys()), sorted(counties.values())) :
    print(f'{key}            {value}')
    