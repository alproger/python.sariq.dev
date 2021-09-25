def tubson_oraliq(start, end) :
    '''kiritilgan oraliqdagi sonlarni ichidan faqat tubsonlarini olib ro\'yhatga
       yozadigan funksiya '''

    tub_sonlar = []
    for n in range(start, end + 1):
        tub = True
        if (n == 1):
            tub = False
        elif (n == 2):
            tub = True
        else:
            for x in range(2, n):
                if (n % x == 0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar


son = tubson_oraliq(1,100)
print(son)