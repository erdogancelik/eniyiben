import os
from os import path
import datetime
from datetime import date, time, timedelta
import time



def main():
    print(os.name)

    print(str(path.exists('textfile.txt')))

    print(str(path.isfile('textfile.txt')))

    print(str(path.isdir('textfile.txt')))

    print(str(path.realpath('textfile.txt')))

    print(str(path.split(path.realpath('textfile.txt'))))

    t = time.ctime(path.getmtime('textfile.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))


main()