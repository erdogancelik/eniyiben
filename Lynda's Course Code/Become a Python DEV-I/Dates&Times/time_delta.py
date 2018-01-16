from datetime import date
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

print(str(datetime.now() + timedelta(days=365)))

t = datetime.now() - timedelta(weeks=4, hours=5, minutes=23)
s = t.strftime('%A %B %d, %Y')
print(s)

today = date.today()
afd = date(today.year,4,1)

time_to_afd = abs(afd - today)
print(time_to_afd.days)


print(t, today)