def summator(*qiymatlar) :
    '''istalgancha sonning yegindisini hisoblovchi funksiya'''
    summa = 0
    for qiymat in qiymatlar :
        summa += qiymat
    
    return summa

def darajator(royhat, daraja = 1) :
    '''1 yoki undan kop bolgan sonlarning kiritilgan darajasini aniqlaydi'''
    darajalar = []
    for qiymat in royhat :
        darajalar.append(qiymat ** daraja)
    
    return darajalar

def kopaytrator(*qiymatlar) :
    '''istalgancha sonning kopaytmasini hisoblovchi funksiya'''
    kopaytma = 1
    for qiymat in qiymatlar :
        kopaytma *= qiymat
    
    return kopaytma