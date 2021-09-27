mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

print(list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)))
