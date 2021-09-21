
pyDict = {
    'int'     : 'butun sonlar tipi',
    'bool'    : 'mantiqiy qiymat tipi',
    'str'     : 'matnlik malumotlar tipi',
    'list'    : 'ro\'yxat',
    'dict'    : 'lug\'at',
    'print()' : 'ekarnga chop etish funksiyasi',
    'input()' : 'kiritish operatori',
    'if-else' : 'shart operatori',
    'len'     : 'malum bir qiymat uzunligi',
    'sort()'  : 'malum bir toplamni saralash',
    'type()'  : 'malumotning tipini aniqlaydi'
}

for key in sorted(pyDict) :
    print(pyDict(key))
    