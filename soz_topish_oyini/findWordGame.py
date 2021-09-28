from uzwords import words
import random

def randomWord():
    '''so'zlar ro'yhai ichidan bitta so'zni ixtiyoriy tanlab beradi'''
    word = random.choice(words)

    return word

def findWord():
    '''funksiya asosiy bo'ib oyinni asosiy mexanizmini boshqaradi'''
    print('Salom so\'z top o\'yiniga hush kelibsiz')
    word = randomWord()
    print(f'Men {len(word)} harfli so\'z o\'yladim topib ko\'ring')

    temp = '-' * len(word)
    print(temp)
    word_list = []

    for w in word :
        word_list.append(w)
    
    index = 0
    while True:
        harf = input('harf kiriting : ')

        if harf in word_list :
            index = word_list.index(harf)
            temp[index] = 'harf'    
        
        else : 
            print('topolmadingiz qayta kiriting')


def play():
    '''O'yinni boshlash uchun asosiy funksiya hech qanday qiymat 
    qabul qilaydi chaqirishingiz bilan o'yinni boshlaydi.'''
    findWord()

    

word = 'salom'

word[1] = 'o'

print(word)
