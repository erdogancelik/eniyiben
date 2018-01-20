""" Trying to Download Things That Don't Exist """

import urllib.request

try:
    webpage = urllib.request.urlopen('https://www.google.com')
    for line in webpage:
        print(line)
except:
    print('Could not access webpage')


