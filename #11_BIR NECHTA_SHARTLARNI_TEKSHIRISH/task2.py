yosh = int(input('Yoshingizni kiriting : '))

narh = 0
if yosh < 4 or yosh > 60 :
    narh = 0

elif yosh < 18 :
    narh = 10_000

else :
    narh = 20_000

print( f' sizga chipta narhi {narh} so\'m')
