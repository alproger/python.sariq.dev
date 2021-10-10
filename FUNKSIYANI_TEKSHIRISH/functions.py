
# function 1
from types import resolve_bases
from unittest import result


def maksimum(son1, son2, son3):
    '''3 ta sonlar ichidan eng kattasini aniqlovchi funksiya'''
    maks = 0
    for num in [son1, son2, son3]:
        if num > maks:
            maks = num 

    return maks

# function 2

def titleFunction(textList):
    '''matnlardan iborat ro'yhat qabul qilib ro'yhatdagi barcha elementlarni
     bosh harfini kattalshtirib beruvchi funksiya'''
    
    for text in range(len(textList)) :
        textList[text] = textList[text].title()
    
    return textList

# function 3

def evenNumberFunction(numberList):
    '''sonlardan iborat ro'yhatni qabul qilib ro'yhatdan faqat juft sonlarni
     ajratib beruvchi funksiya '''
    
    evenNums = [number for number in numberList if number % 2 == 0]

    return evenNums

# function 4

def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        x = fib(n-1)
        # the new element the sum of the last two elements
        x.append(sum(x[:-3:-1]))
        return x

def get_fib(number):
    result = False
    if number in fib(100):
        result = True
    return result

     

 



