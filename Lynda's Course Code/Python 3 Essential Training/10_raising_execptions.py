
def main():
    try:
        fh = open('lines.txt')
        for line in fh:
            print(line.strip())
    except IOError as e:
        print('cannot read', e)
    except ValueError as e:
        print('bad filename', e)



main()