import datetime

now = datetime.datetime.now()

print(now) #2018-01-12 19:59:15.838680

print(now.strftime('%A %D %B %Y')) #Friday 01/12/18 January 2018

print(now.strftime('%c, %x, %X'))  #Fri Jan 12 19:59:15 2018, 01/12/18, 19:59:15

print(now.strftime('%I:%M:%S %p')) #07:59:15 PM

print(now.strftime('%H:%M'))       #19:59

