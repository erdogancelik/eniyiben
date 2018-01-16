class Adder:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        self.data += other


class AddBoth(Adder):
    def __init__(self, value):
        Adder.__init__(self, value)

    def __add__(self, other):
        return Adder.__add__(self, other)

    def __str__(self):
        return '[Value:{}]'.format(self.data)

    def __repr__(self):
        return 'AddBoth({})'.format(self.data)


X = AddBoth(4)
print(X, str(X), repr(X))

X.__add__(1)
print(X, str(X), repr(X))

