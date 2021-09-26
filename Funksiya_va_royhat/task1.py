def katta_harf(royhat) :
    '''Ro'yhat qabul qilib ro'yhatdagi sozlarni bosh harfini 
     katta qilib beruvchi funksiya'''
    Royhat = []
    while royhat :
        katta = royhat.pop
        Royhat.append(katta.title())

    Royhat = Royhat[-1:]
    return Royhat

ismlar = ['ali', 'vali', 'hasan', 'husan']

katta_harf(ismlar)

print(ismlar)
         
