def maksimal(num1, num2, num3):
    '''3 ta son qabul qilib ulardan eng kattasini chiqaruvchi funksiya'''
    max = 0
    for num in [num1, num2, num3] :
        if max < num :
            max = num
    
    return max

    
maks = (maksimal(1, 2, 3))
print(maks)