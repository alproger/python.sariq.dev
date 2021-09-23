savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:

    qiymat = input(savol)

    if qiymat.title() == 'Exit':
        break

    elif float(qiymat) < 0:
       continue
    
    else:
    
        ildiz = float(qiymat)**(0.5)
        
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
