def gen(args):

    while 0<args:
        yield args
        args -=1


for i in gen(10):
    args=-1
    print(i, end=',')