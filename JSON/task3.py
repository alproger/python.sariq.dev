import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# data malumotini data.json fayl sifatida saqlash 
with open('data.json', 'w') as jfile :
    json.dump(data, jfile)

# talaba_json malumotini talaba.json fayl sifatida saqlash 
with open('talaba.json', 'w') as jfile :
    json.dump(talaba_json, jfile)

