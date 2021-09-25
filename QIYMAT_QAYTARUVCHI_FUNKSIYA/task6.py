def fibonachi(son):
    '''son qabul qilib shu son qiymaticha fibonachi ketmaketligini
     qaytaruvchi funksiya'''
    fibo = []
    for i in range(son):
        if i == 0 or i == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[i-1]+fibo[i-2])
    return fibo
print(fibonachi(10))