class A:
    __slots__ = ['a', 'b']


class B(A):
    __slots__ = ['d', '__dict__']


X = B()

X.a = 1;
X.d = 3;
X.c = 5

print(X.a, X.c, X.__slots__)