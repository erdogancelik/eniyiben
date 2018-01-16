class Adders:
    def __init__(self, value):
        self.amount = value

    def __add__(self, other):
        print('add')
        return self.amount + other

    def __radd__(self, other):
        print('radd')
        return other + self.amount

    def __iadd__(self, other):
        print('iadd')
        self.amount += other
        return self.amount

        # There are some other options to write the same code here are some __radd__ options

        # def __radd__(self, other):
        #   self.__add__(other)

        #   self + other

        # __radd__ = __add__


X = Adders(5)
print(X + 1)

Y = Adders(99)
print(1 + Y)

Z = Adders(33)
Z += 1
print(Z)

print(X + Y)
