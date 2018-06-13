import datetime

format = "%Y-%m-%d"

today = datetime.datetime.today()


s = today.strftime(format)



war_start = '2011-01-03'

print(datetime.datetime.strptime(war_start, format))
print('strftime:', s)
print('Normal     :', today)
