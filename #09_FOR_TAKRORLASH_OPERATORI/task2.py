numbers = []
for i in range(10,100):
    if i % 2 != 0 :
        numbers.append(i)

for number in numbers :
    text = f' {number}ning kubi : {number ** 3}'
    print(text)
