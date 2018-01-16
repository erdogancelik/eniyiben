# This example lets us understand/help to run same loop more than once

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.number = 0

    def __next__(self):
        if self.number >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.number]
            self.number += 2
            return item


if __name__ == '__main__':
    alphabet = 'abcdefghjk'
    skipper = SkipObject(alphabet)
    I = iter(skipper)
    print(next(I), next(I), next(I))

# Below and above example has the same mentality they both loop

    for x in skipper:
        for y in skipper:
            print(x+y, end=' ')
