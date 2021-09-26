def bahola(royhat):
    '''Royhatdagi talaba yoki o'quvchilarni baholovchi funksiya
       funksiya natijani lug'at ko'rinishida qaytaradi'''
    
    baholanganlar = {}
    print('talabalarni baholaymiz')
    
    for ism in royhat :
        baholanganlar[ism] = int(input(f'{ism.title()}ning bahosi : '))
    
    return baholanganlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
print(bahola(ismlar))
print(ismlar)

