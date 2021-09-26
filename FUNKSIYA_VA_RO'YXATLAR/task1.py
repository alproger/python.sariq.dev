def katta_harf(royhat) :
    '''Ro'yhat qabul qilib ro'yhatdagi sozlarni bosh harfini 
     katta qilib beruvchi funksiya'''
    Royhat = []
    for element in royhat :
        Royhat.append(element.title())
    
    return Royhat

ismlar = ['ali', 'vali', 'hasan', 'husan']

katta_harf(ismlar)

print(ismlar)
         
