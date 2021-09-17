taomlar = ['osh', 'mastava', 'kabob', 'manti', 'somsa'] 
nonushta = taomlar.copy()

#taomlarni olib tashlaymiz
nonushta.remove('osh')
nonushta.remove('mastava')

#taom qo'shamiz
nonushta.append('quymoq')
nonushta.append('shirinlik')

print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq' #qo'shib bo'lmaydi.

