mahsulotlar = ['non', 'go\'sht', 'olma', 'kofe', 'sabzi', 'guruch', 'choy', 'pepsi', 'shirinlik', 'kanfet', 'sut', 'pishloq']
savat = []

print('Savatchaga 5 ta mahsulot qo\'shing  ')

for i in range(0, 5):
    mahsulot = input('{}-mahsulot : '.format(i+1))
    savat.append(mahsulot)


for i in savat :
    if i in mahsulotlar:
        print('Bizda {} bor'.format(i))
    else :
        print('bizda {} yo\'q'.format(i))
