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

state = input('Davlat nomini kiriting : ')

if state.title() in counties.keys() :
    print(f'{state.title()}ning poytaxti : {counties[state]}') 

else:
    print('Bizda bunday ma\'lumot yo\'q !')