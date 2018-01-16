class Thruty:
    def __bool__(self):
        return True

X = Thruty()
print(bool(X))


class Len:
    def __len__(self):
        return 0

Y = Len()
if not Y:
    print('Negative')


# Python always looks __bool__ first rather than __len__