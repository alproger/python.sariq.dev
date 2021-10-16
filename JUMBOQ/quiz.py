import random


#my way
numbers = list(range(1, 101))
number = random.randint(1, 101)
numbers.remove(number)
print(number)
print(sum(range(1,101)) - sum(numbers))
