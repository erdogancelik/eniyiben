class Selfless:
    def __init__(self, number):
        self.number = number

    def selfless(arg1, arg2):
        return arg1 + arg2

    def normal(self, arg1, arg2):
        return self.number + arg1 + arg2


X = Selfless(5)
print(X.normal(2,3))
print(Selfless.selfless(1,2))
print(Selfless.normal(X,1,2))

# This 2 examples below fails look carefully

print(X.selfless(7,8))
print(Selfless.normal(5,6))