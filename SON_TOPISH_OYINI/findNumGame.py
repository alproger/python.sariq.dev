import random
from typing import Tuple

def user_think():
    '''foydalanuvchi son p'ylaydi kompyuter topishga urinadi'''    
    taxmin_pc = 0

    startRandom = 1
    endRandom = 10
    
    ishora = True
    while ishora :
        
        number = random.randint(startRandom, endRandom)
        
        sorov = f"siz o'ylagan raqam {number} mi ? (ha) (+)-katta, (-)-kichik) "
        inputUser = input(sorov)
        taxmin_pc += 1

        if inputUser.lower() == 'ha':
            print(f'men {taxmin_pc}ta taxminda topdim')
            
            ishora = False
        else :
         
            if inputUser == '+' :
                startRandom = number + 1 
        
            elif inputUser == '-' :
                endRandom = number  - 1
        
    return taxmin_pc


def pc_think():
    '''bu funskiyada kompyuter raqam o'ylaydi topishingiz kerak'''
    number = random.randint(1,11)
    taxmin_user = 0
    
    print('men raqam o\'yladim  siz uni topishga uruning')
    
    while True:
        inputNum = int(input('raqam kiriting : '))
        taxmin_user += 1
        
        if inputNum == number :
            print(f'{taxmin_user} ta taxminda topdingiz tabriklayman ')
            break
            

        else :
            help = ''
            
            if number > inputNum :
                help = 'topolmadingiz men o\'ylagan son bundan katta'
            
            else :
                help = 'topolmadingiz men o\'ylagan son bundan kichik'

            print(help)

    return taxmin_user





def play():
    '''bu funksiya o'yinni boshlash uchun  ishlatiladi yani funksiya hech qanday argument qabul qilmaydi
       chaqirilganda bizning o'yin boshlanadi'''

    shart = '''Salom siz raqamni top o'yiniga start berdiz. 
               
               O'yin shartlari :
                *men raqam o'ylayman siz topshingiz kerak
                *siz raqam o'ylaysiz men topishim kerak
                *raqamlar 1-10 oraliqda bo'lishi kerak
                *kim kam taxmin bilan topsa osha g'olib bo'ladi
                
                '''
    print(shart)

    start = input("o'yinni boshlash uchun ixtiyoriy tugmani bosing : ")

    if start == '' or start != None :
        print('Oyin boshlandi')

        while True : 
            pc = pc_think()
            print('Endi siz son o\'ylang men topishga urunib ko\'raman')
            sorov = input('Oylab bolgan bo\'lsangiz enterni bosing ')
            if sorov == '':
                user = user_think()

            if user > pc :
                print('siz yutdingiz')

            elif user == pc :
                print('Durrang')
            
            else :
                print('men yutdim')

            sorov1 = input('Yana o\'ynaysizmi ? (ha/yo\'q)')

            if sorov1 == "yo'q" :
                break

