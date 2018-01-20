""" Scrubbing A Stubborn Pan """

import random


dirty = True
scrub_count = 0

while dirty:

    scrub_count +=1
    print('Scrub the pan: {}'.format(scrub_count))

    print('Rinse & check if the pan is clean')

    x = random.randint(0,9)

    if x == 0:
        print('All clean')
        dirty = False
    else:
        print('Still dirty')




