def search_birth(birthday):
    '''fayl nomi orqali file ichidagi pi sonini ichida 
    tug'ulgan kun oy yilim borligini aniqlaydi, masalan '''
    
    with open('task2.txt') as file :
        info = file.read()
    
    if birthday in info:
        return f'{input} pi ning qiymati ichida mavjud' 
    
    else:
        return f'mavjud emas'

result = search_birth('712268066')
print(result)