[**<h1>#17 WHILE TSIKLI</h1>**](https://python.sariq.dev/while/17-while-loop#yana-input)

<h3>AMALIYOT</h3>

**<h4>#1</h4>**
Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

**<h4>#2.1</h4>**
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

**<h4>#2.2</h4>**
Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)

**<h4>#3</h4>**
Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?


 savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
 
savol += "Musbat son kiriting "

savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:

    qiymat = input(savol)

    if qiymat<0:
    
       continue
    
    elif qiymat=='Exit':
    
        break
    
    else:
    
        ildiz = float(qiymat)**(0.5)
        
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
