import random

numbers = list(range(1, 101))
number = random.randint(1, 101)
numbers.remove(number)
print(number)
sums = 100 * 101 / 2
print(int(sums - sum(numbers)))
