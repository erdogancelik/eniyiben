import re


def main():
    fh = open('lines.txt')
    pattern = re.compile('(a|i)n', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('###', line), end='')

main()