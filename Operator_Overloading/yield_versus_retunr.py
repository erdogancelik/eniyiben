def gen(x):
    for i in range(x):
        yield i ** 2

for my in gen(5):
    print(my)

def deneme(y):
    t = []
    for i in range(y):
        t.append(i**2)
    return t

for ym in deneme(5):
    print(ym)