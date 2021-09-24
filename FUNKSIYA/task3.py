def jufttoq_aniqla(qiymat):
    
    '''Foydalanuvchidan son olib, son juft yoki
       toqligini konsolga chiqaruvchi funksiya'''

    result = f'{qiymat} soni '
    
    if int(qiymat) % 2 == 0 :
        result += 'juft son'
    
    else:
        result += 'toq son '

    print(result)

son = int(input('son kiriting : '))
jufttoq_aniqla(son)


