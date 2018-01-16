class Callee:
    def __call__(self, *args, **kwargs):
        print('Callee:', args, kwargs)


T = Callee()
print(T(7,8,9))


P = Callee()
print(P(1, 2, 3, x=4, y=5))


class Prod:
    def __init__(self, value):
        self.amount = value

    def __call__(self, other):
        return self.amount * other


X = Prod(7)
print(X(7))
