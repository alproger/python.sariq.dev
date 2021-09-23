
buyurtmalar = []

while True :

    savol = 'buyurtma kiriting : '
    buyurtma = input(savol)
    
    savol += 'yana buyurtma kiritasizmi ? (ha/yo\'q)'
    if buyurtma != 'yo\'q' :
        buyurtmalar.append(buyurtma)

    else :
        break

