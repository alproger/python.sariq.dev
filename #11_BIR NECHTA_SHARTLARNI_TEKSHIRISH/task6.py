foydalanuvchilar = ['Sarvar', 'Bahrom', 'Doniyor', 'Murodil', 'Asadbek']

login = input('Login tanlang : ')

result  = ''

if login in foydalanuvchilar:
    result = 'Bu login band boshqa login tanlang'

else:
    result = 'Xush kelibsiz foydalanuvchi'

print(result)