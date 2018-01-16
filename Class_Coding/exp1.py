class Super:
    def method(self):
        print('in Super method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('I am the replacer')

class Extender(Super):
    def method(self):
        print('start Extender')
        Super.method(self)
        print('ending Extender')

class Provider(Super):
    def action(self):
        print('I am the provider')


if __name__ == '__main__':
    # for klass in [Inheritor, Replacer, Extender]:
    #     print(klass.__name__)
    #     klass().method()

    x = Provider()
    x.delegate()



