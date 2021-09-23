'''
#ishora 
ishora = True
while ishora :
    yosh = (input('yoshingizni kiriting : '))
    ticket = 0

    if yosh == 'quit' or yosh == 'exit':
        ishora = False
    
    else :
        if int(yosh) < 7 :
            ticket = 2000
    
        elif 7 < int(yosh) <= 18 :
            ticket = 3000
    
        elif 18 < int(yosh) < 65 :
            ticket = 10000

    # 65 dan kattani tekshirish shart emas yuqoridagi shartlarga 
    # tushmasa aniq 65 dan katta yosh kirilgan bo'ladi
        print(f'chipta sizga {ticket} so\'m')
'''

''''
#shart tekshirish
yosh = ''
while yosh != 'quit' or yosh != 'exit' :
    yosh = (input('yoshingizni kiriting : '))
    ticket = 0

    if yosh == 'quit' or yosh == 'exit':
        ishora = False
    
    else :
        if int(yosh) < 7 :
            ticket = 2000
    
        elif 7 < int(yosh) <= 18 :
            ticket = 3000
    
        elif 18 < int(yosh) < 65 :
            ticket = 10000

    # 65 dan kattani tekshirish shart emas yuqoridagi shartlarga 
    # tushmasa aniq 65 dan katta yosh kirilgan bo'ladi
        print(f'chipta sizga {ticket} so\'m')

'''
