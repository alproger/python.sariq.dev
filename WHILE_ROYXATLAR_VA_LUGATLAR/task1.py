
buyurtmalar = []

savol1 = 'buyurtma kiriting : '
savol2 = 'yana buyurtma berasizmi ? (ha/yo\'q) '
while True :
    
    buyurtma = input(savol1)
    buyurtmalar.append(buyurtma)
    sorov = input(savol2)

    if sorov == 'yo\'q' :
        break

    
print('buyurtmalaringiz ro\'yhati ')
for buyurtma in buyurtmalar :
    print(buyurtma)

