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
    
    saveWord = word    
    newWord = ''
    index = 0

    wordlist = list(len(word) * '-')
    inputedWords = []

    count = 0

    while True :
        for w in wordlist :
            print(w, end='')
        
        word_input = input('\n\nharf kiriting : ')
        count += 1

        inputedWords.append(word_input)
        inputed = ''.join([str(element) for element in inputedWords])
        print(f'\nsiz kiritgan harflar : {inputed}')
        
        if word_input in word :
            index = word.find(word_input)
            wordlist.insert(index, word_input)
            newWord = ''.join([str(elem) for elem in wordlist])
            del wordlist[index+1]
            
            word = word.replace(word_input, ' ', 1)
        
        newWord = newWord.replace('-','')

        if saveWord == newWord :
            result = f'\nso\'z "{newWord}" edi \nSiz {count} ta urunishda so\'zni topdingiz'
            print(result)
            break


def play():
    '''O'yinni boshlash uchun asosiy funksiya hech qanday qiymat 
    qabul qilaydi chaqirishingiz bilan o'yinni boshlaydi.'''
    findWord()
