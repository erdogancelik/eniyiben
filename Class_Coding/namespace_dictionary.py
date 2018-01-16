class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

X = Sub()

print(X.__dict__)
print(X.__class__)
print(Super.__bases__)
print(Sub.__bases__)

X.hello()

print(X.__dict__)

X.hola()

print(X.__dict__)

print(X.data1, X.__dict__['data1'])

X.__dict__['data3'] = 'ham'

print(X.__dict__)

print(dir(X))


for i in dir(X):
    if not i.startswith('__'):
        print(i)

print([i for i in dir(X) if not i.startswith('__')])

print(X.__dict__.keys())