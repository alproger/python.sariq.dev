
ebozor = {}
print('e bozor uchun mahsulotlar va ularning narxini kiritamiz')

while True:
    
    mahsulot = input('mahsulot nomini kiriting : ')
    narx = input(f'{mahsulot}ning narxini kiriting : ')

    ebozor[mahsulot] = int(narx)

    savol = input('yana mahsulot qo\'shasizmi ? (ha/yo\'q) : ')

    if savol == 'yo\'q' :
        break

for mahsulot, narx in ebozor.items():
    info = f'{mahsulot}ning narxi : {narx}'
    print(info)

