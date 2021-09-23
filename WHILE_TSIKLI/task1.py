
kitoblar  = []
while True :
    
    kitob = input('Sevimli kitobingizni kiriting : ')
    
    if kitob.lower() == 'stop' :
        break
    
    else:
        kitoblar.append(kitob)

print('Dastur tugadi ! ')
