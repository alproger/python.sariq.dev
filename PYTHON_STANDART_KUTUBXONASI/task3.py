import datetime as dt
my_born_day = dt.datetime(1998, 1, 3, 7, 0, 0)
today = dt.datetime.now()

farq_kun = (today - my_born_day).days
farq_sekund = (today- my_born_day).seconds 
farq_minut = int(farq_sekund / 60)
farq_soat = int(farq_minut / 60)

farq_sekund -= farq_minut * 60
farq_minut -= farq_soat * 60


info = f"Tug'ulgan kunimdan boshlab {farq_kun} kun {farq_soat} soat {farq_minut} minut {farq_sekund} sekund o'tdi "
print(info)