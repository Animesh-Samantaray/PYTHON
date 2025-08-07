import datetime 
print(f'datetime --->{datetime.datetime.now()}')
print(f' today  {datetime.datetime.today()}')
new = datetime.date(2025,4,16)
print(new)
tm=datetime.time(10,20) #hr,min
print(tm)

delta = datetime.timedelta(days=1)
yesterday = datetime.datetime.now() - delta
print(yesterday)
