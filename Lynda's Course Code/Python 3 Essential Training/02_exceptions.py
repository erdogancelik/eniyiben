
try:
    fh = open('lines.txt', 'r')
    for lines in fh.readlines():
        print(lines)
except:
    print('There is a error')
    raise Exception


