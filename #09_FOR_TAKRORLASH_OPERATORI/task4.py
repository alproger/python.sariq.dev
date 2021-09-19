count = int(input('Bugun nechta odam bilan suhbatlashdingiz : '))

suhbatdoshlar = []

for i in range(count):
    suhbatdosh = input(f'{i+1}-suhbatdosh ismi : ')
    suhbatdoshlar.append(suhbatdosh)

print(suhbatdoshlar)