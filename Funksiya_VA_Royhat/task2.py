def katta_harf(royhat) :
    '''Ro'yhat qabul qilib ro'yhatdagi sozlarni bosh harfini 
     katta qilib beruvchi funksiya'''
    katta = []
    for matn in royhat :
        katta.append(matn.title())
    
    return katta


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)