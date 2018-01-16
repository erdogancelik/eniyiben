class Indexer_a:
    def __getitem__(self, item):
        return item ** 2


Z = Indexer_a()
print(Z[2])

for i in range(5):
    print(Z[i])


class Indexer_b:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]


P = Indexer_b()
print(P[0])
print(P[1:])
print(P[1:3])


class Indexer_c:
    def __getitem__(self, item):
        if isinstance(item, int):
            print('indexing:', item)
        else:
            print('slicing', item.start, item.stop, item.step)


A = Indexer_c()
print(A[2])
print(A[1:99:2])


class StepperIndex:

    def __getitem__(self, i):
        return self.data[i]


H = StepperIndex()
H.data = 'erdogan'
print(H[1])
print([i for i in H])
