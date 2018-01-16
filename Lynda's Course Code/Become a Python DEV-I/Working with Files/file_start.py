
def write_file():
    f = open("textfile.txt", 'w')

    for i in range(10):
        f.write('This is the line {}\n'.format(i+1))

    f.close()


def append_file():
    f = open("textfile.txt", 'a')

    for i in range(10):
        f.write('This is the line {}\n'.format(i+1))

    f.close()


def read_file():
    f = open("textfile.txt", 'r')

    #This for reading the whole file
    contents = f.read()
    print(contents)

    # This is also reads the whole file
    fl = f.readlines()
    for x in fl:
        print(x)

read_file()