class Comp:
    data = 'spam'

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


X = Comp()

print(X > 'ham', X < 'ham')
   