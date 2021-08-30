import datetime

my_time = datetime.datetime.utcnow()
print(my_time)

today = datetime.date.today()

print(today.__format__("%d/%m/%Y"))
print(today.strftime("%d/%m/%Y"))