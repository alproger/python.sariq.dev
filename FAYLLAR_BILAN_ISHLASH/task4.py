from os import WIFCONTINUED
import pickle
with open('task2.txt') as file:
    piNums = file.readlines()

piNums = [pi.strip() for pi in piNums]
PI = ''.join(pi for pi in piNums)

with open('PINUM.pcl', 'wb') as file :
    pickle.dump(PI, file)



with open ("PI.pcl", 'rb') as file :
    pi = pickle.load(file)

print(pi)