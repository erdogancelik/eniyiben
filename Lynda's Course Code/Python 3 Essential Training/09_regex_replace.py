
import re

def main():
    fh = open('lines.txt')
    for line in fh:
        print(re.sub('(a|i)n', '###',  line), end=' ')


main()