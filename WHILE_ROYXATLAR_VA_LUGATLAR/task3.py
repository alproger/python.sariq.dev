ebozor = {
            'non'       : 2000, 
            'olma'      : 5000, 
            'anor'      : 23000, 
            "go'sht"    : 75000, 
            'kartoshka' : 6000, 
            'sabzi'     : 13000, 
            'piyoz'     : 4500, 
            'nok'       : 7000
                                    }

buyurtmalar = ['olma', 'non', "go'sht", 'anor', 'gilos', 'pepsi', 'qalampir', 'karam']

for buyurtma in buyurtmalar:
    if buyurtma in ebozor.keys():
        print(f'{buyurtma}ning narxi {ebozor[buyurtma]} so\'m')
    
    else:
        print(f'Bizda {buyurtma} yo\'q')