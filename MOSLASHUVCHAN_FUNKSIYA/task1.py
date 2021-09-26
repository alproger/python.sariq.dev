def kopaytir(*sonlar):
    '''istalgancha son qabul qilib sonlarning ko'paytmasini chiqaradi'''
    if sonlar :
        natija = 1
        
    else:
        natija = 0
    
    for son in sonlar:
        natija *= son
    
    return natija


print(kopaytir(1,2,3,4,5))
print(kopaytir())

    