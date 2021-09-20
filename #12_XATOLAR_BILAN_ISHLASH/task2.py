yosh = int(input("Yoshingiz nechida? "))  # bu yerda tip ko'rsatilishi kerak edi int

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18 : # : qolib ketgan
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm") # probel surish kerak edi
