oilam = {}
for i in range(3) : 
    ism = input('ismingizni kiritng : ')
    print(f'{ism} 3 ta sevimli kinoyingizni kiriting ')
    
    oilam[f"{ism}"] = [] # oilam noli lug'atga kiritilgan ismni kalit qilib kalitga royhat qoshilyapti

    for kino in range(3): 
        oilam[f"{ism}"].append(input(f'{kino+1}-kino : '))
        

for ism in oilam.keys():
    print(f'{ism}ning sevimli kinolari')

    for kino in oilam[ism] :
        print(kino)
    print()



