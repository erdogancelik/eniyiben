class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattribute__(self, item):
        print('Trace:' + item)
        return getattr(self.wrapped, item)


x = Wrapper({'a': 1, 'b':2})
print(list(x.keys()))
