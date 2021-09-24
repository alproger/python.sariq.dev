def daraja_oshir(qiymat):

    """qiymat qabul qilib qiymatning
        kvadrati va kubini hisoblovchi funksiya"""
    
    result =  f'{qiymat}ning kvadrati {qiymat ** 2}'
    result += f'\n{qiymat}ning kubi {qiymat ** 3}'

    print(result)


son = float(input(f"son kiriting : "))
daraja_oshir(son)

