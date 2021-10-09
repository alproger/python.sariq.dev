import json

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
ism = talaba['ism']
fam = talaba['familiya']
print(f'{ism} {fam}')
