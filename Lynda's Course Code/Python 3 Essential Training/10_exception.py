
def main(text):
    try:
        fh = open('{}.txt'.format(text))
    except IOError as e:
        raise ('File could not opened', e)
    else:
        for lines in fh.readlines():
            print(lines.strip())


main('lines')



def main_(text):
    try:
        fh = open('{}.txt'.format(text))
    except:
        raise ('File could not opened')
    else:
        return fh


x = main_('lines')
print(x)