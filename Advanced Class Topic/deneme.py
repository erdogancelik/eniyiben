class getattributes(object):
    def getage(self):
        return 40

    def setage(self, value):
        print('set: {} {}'.format('number', value))
        self._age = value

    age = property(getage, setage, None, None)


x = getattributes()

print(x.age)
x.age =42
print(x._age)

