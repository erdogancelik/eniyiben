import re

def main():
    fh = open('lines.txt')
    for line in fh:
        if re.search('(a|i)n', line):
            print(line, end='')

main()