numbers = list(range(2,11))
number = int(input('Son kiriting : '))

for num in numbers : 
    if number % num == 0 :
        result = f'{number} soni {num}ga qoldiqsiz bo\'linadi ! '
        print(result)
