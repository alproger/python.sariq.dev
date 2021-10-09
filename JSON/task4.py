import json

with open('students.json', 'r') as jfile :
    students = json.load(jfile)

for student in students['student'] :
    
    ism = f'{student["name"]}'
    familiya = f'{student["lastname"]}'
    kurs = f'{student["year"]}'
    fakultet = f'{student["faculty"]}'
    
    info = f'{ism} {familiya}, {kurs}-kurs, {fakultet} talabasi '
    print(info)

