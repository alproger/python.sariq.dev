import re

andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
telRaqam = input('Telefon raqam kiriting : ')
natija = re.match(andoza, telRaqam)

if natija == None:
    print('Raqam kiritilmadi')
else:
    print('Rahmat')

