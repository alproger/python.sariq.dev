python = {
    'if-else' : 'shart operatori',
    'str'     : 'matn tipi ',
    'dict'    : 'lug\'at ',
    'list'    : 'ro\'yhat',
    'int'     : 'butun son tipi',
    'float'   : 'qoldiqli son tipi',
    'print()' : 'ekranga chop etish funksiyasi',
    'input()' : 'kiritish operatori',
    'for'     : 'tsikl operatori',
    'break'   : 'malum jarayonni to\'xtatish',
    'continue': 'malum bir jarayonni o\'tkazib yuborish',
    'len'     : 'malum bir qiymat uzuzligi',
    'or'      : 'shart operatori "yoki"',
    'and'     : 'shart operatori "va"',
    'not'     : 'inkor shart operatori',
    'in'      : 'ichida malum bir qiymat ichida ',
    'range'   : 'malum bir oraliq yoki ketma-ketlik'
}

key = input('biron bir so\'z kiriting : ')

result = python.get(key,'Bunday so\'z mavjud emas !')

print(result)
