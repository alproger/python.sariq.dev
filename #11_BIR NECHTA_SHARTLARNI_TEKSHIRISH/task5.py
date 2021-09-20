mahsulotlar = ['non', 'go\'sht', 'olma', 'kofe', 'sabzi', 'guruch', 'choy', 'pepsi', 'shirinlik', 'kanfet', 'sut', 'pishloq']
savat = []

bor_mahsulot = []
mavjud_emas = []

print('Savatchaga 5 ta mahsulot qo\'shing  ')

for i in range(0, 5):
    mahsulot = input('{}-mahsulotni qo\'shing : '.format(i+1))
    savat.append(mahsulot)


for i in savat :
    if i in mahsulotlar:
        bor_mahsulot.append(i)

    else :
        mavjud_emas.append(i)

if mavjud_emas :
    print(f'Do\'konimizda quyidagi mahsulotlar yo\'q :')
    for i in mavjud_emas :
        print(i)

else :
     print(f'Do\'konimizda siz so\'ragan barcha mahsulotlar bor ')