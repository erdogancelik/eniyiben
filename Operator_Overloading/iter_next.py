# We can only use looping only once because __iter__ only 'return self'

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop


    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration

        else:
            self.value += 1
            return self.value ** 2


X = Squares(1, 5)

for i in X:
    print(i, end=' ')

print([a for a in X])

a = 36 in Squares(1,10)
print(a)

a, b, c = Squares(1,3)
print(a, b, c)

d = ':'.join(map(str, Squares(1,5)))
print(d)

def gsqaures(start, stop):
    for p in range(start, stop+1):
        yield p ** 2

for m in gsqaures(1,5):
    print(m, end=' ')


for h in (x**2 for x in range(1,6)):
    print(h, end=' ')


