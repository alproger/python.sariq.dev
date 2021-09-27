import random

def Lotoreya(oyinchilar):
    '''Funksiya foydalanuvchilar ro'yhatini kiriting va funksiya yutuqni yutgan 
       foydalanuvchini aniqlab beradi'''
    
    golib = random.choice(oyinchilar)
    
    return f'{golib} tabriklaymiz 1.000.000 $ yutdingiz'

def OmadliRaqam(raqamlar):
    '''Raqamlar ichidan omadlisini aniqlab beruvchi funksiya va raqamga 
    tegishl sovg'ani aniqlab beradi'''
    omadlik = random.choice(raqamlar)
    
    sovga = ''

    if omadlik in list(range(1,11)) :
        sovga = f'{omadlik} raqam uchun sovga 1.000.000 $ yutdingiz '

    elif omadlik in list(range(10,31)) :
        sovga = f'{omadlik} raqam uchun sovga 500.0000 $ yutdingiz '
    
    elif omadlik in list(range(30,50)) :
        sovga = f'{omadlik} raqam uchun sovga 10.000 $ yutdingiz '

    else :
        sovga = f'{omadlik} Afsuski omadsiz raqam'

    return sovga 


