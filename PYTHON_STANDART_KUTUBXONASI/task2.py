import datetime as dt

bugun = dt.date.today()
ramazon = dt.date(2022, 4, 2)
qurban_eid = dt.date(2022, 7, 9)
farq_ramazon = ramazon - bugun
farq_qurban_eid = qurban_eid - bugun
# print(farq)
print(f"Ramazonga {farq_ramazon.days} kun qoldi")
print(f"Qurbon hayitga {farq_qurban_eid.days} kun qoldi")