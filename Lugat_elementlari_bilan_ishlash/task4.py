menu = {
    'non'      : 2000,
    'choy'     : 1000,
    'kabob'    : 15000,
    'manti'    : 4000,
    'norin'    : 20000,
    'dimlama'  : 25000,
    'palov'    : 20000,
    'somsa'    : 9000,
    'tovuq'    : 22000,
    'sho\'rva' : 10000
}
foods = []
print('3ta taom tanlang')
for i in range(3):
    foods.append(input(f'{i+1}-taom : '))

for food in foods :
    if food.lower() in menu.keys() :
        print(f'{food} {menu[food]} so\'m')
    else:
        print(f'Kechirasiz bizda {food} yo\'q')
