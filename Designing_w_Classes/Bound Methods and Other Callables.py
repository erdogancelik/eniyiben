class Number:
    def __init__(self, number):
        self.number = number

    def double(self):
        return self.number * 2

    def triple(self):
        return self.number * 3

x = Number(2)
y = Number(3)
z = Number(4)

acts = [x.double, y.double, z.triple]
for act in acts:
    print(act())


bound = x.double
print(bound.__self__, bound.__func__)
print(bound())