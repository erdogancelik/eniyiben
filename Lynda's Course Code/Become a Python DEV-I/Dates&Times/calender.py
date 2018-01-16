import calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(1985, 6, 0, 0)
print(str)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
src = hc.formatmonth(1985, 6)
print(src)

for i in c.itermonthdays(1985, 6):
    print(i)

for day in calendar.day_name:
    print(day)