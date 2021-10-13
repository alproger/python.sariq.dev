import datetime as dt

start_date = dt.date.today()
delta_date = dt.timedelta(14)

i = 0
while i <= 10 :
    print(start_date)
    start_date += delta_date
    i += 1