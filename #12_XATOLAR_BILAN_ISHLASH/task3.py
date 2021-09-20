x = float(input("Birinchi sonni kiriting: ")) # qavs yopilmagan edi
y = float(input("Ikkinchi sonni kiriting: ")) # qavs yopilmagan edi
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}') # '' yoki "" bolishi kerak edi
else : # : qolib ketgan edi
    print(f"{x}>{y}")