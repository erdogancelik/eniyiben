import sys
import os
import urllib.request
import random
import datetime


def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd)
    print(os.urandom(25))

    page = urllib.request.urlopen('https://google.com')
    for line in page:
        print(str(line))

    print(random.randint(1,1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.hour, now.minute, now.second, now.microsecond)





main()