
#class User for registration to website new users with metods

class User :
    ''''Websayt uchun foydalanuvchilarni ro'yhatga olish uchun tuzulgan klass'''
    
    def __init__(self, name, surname, username, mail, password):
        '''User klasining qiymat yoki hususiyatlarni saqlash funksiyasi'''

        self.name = name
        self.surname = surname
        self.username = username
        self.mail = mail
        self.password = password

    def get_info(self):
        '''User klasining metodi, bu metod foydalanuvchi haqida to'liq malumot 
        qaytaradi consolega chiqarmaydi parol malumotini qaytarmaydi. '''
        info = f'foydalanuvchi : "{self.username}" {self.name} {self.surname} mail manzili : {self.mail}'
        return info
    
    def get_name(self):
        '''Foydalanuvchini ismini qaytaruvchi metod'''
        return self.name
    
    def get_surname(self):
        '''Foydalanuvchining familiyasini qaytaradi'''
        return self.surname
    
    def get_mail(self):
        '''foydalanuvchi ro'yhatdan o'tgan mail addresini qaytaruvchi metod'''
        return self.mail
    
    def get_username(self):
        '''foydalanuvchi tanlagan usernameni qaytaruvchi metod'''
        return self.username
    
    def get_password(self):
        '''foydalanuvchi kiritgan parolni qaytaruvchi metod'''
        return self.password

user1 = User('Jon', 'Tomson', 'jorj01', 'tomson@mail.com', '#12345')

print(user1.get_info())
print(user1.get_name())

