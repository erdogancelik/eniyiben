class A:
    pass

class B(A):
    pass

print(B.__bases__)
print(B.__name__)

print(A.__bases__)
print(A.__name__)

X = B()

print(X.__dict__)
print(X.__class__)