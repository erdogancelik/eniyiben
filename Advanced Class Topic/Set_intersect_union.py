class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in self.data:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)


x = Set([1, 2])
print(x.intersect([3, 4]))
