import random

f_read = open('lines.txt', 'r')
f_write = open('new_file{}.txt'.format(random.random()), 'w')

reading = f_read.read()

f_write.write(reading)
