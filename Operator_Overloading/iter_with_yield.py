class Squares_Yield:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


for i in Squares_Yield(1,5):
    print(i, end=' ')

