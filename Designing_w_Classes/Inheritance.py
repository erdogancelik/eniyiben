class Employee:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def give_raise(self, increase):
        self.money = self.money + (self.money * increase)

    def what_does(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return "Employee name={0}, salary={1}".format(self.name, self.money)


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def what_does(self):
        print(self.name, 'helps for customer\'s order')


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def what_does(self):
        print(self.name, 'Prepares the pizza dough')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def what_does(self):
        print(self.name, 'Cooks the great pizzas')


if __name__ == '__main__':

    bob = PizzaRobot('Bob')
    print(bob)
    bob.what_does()
    bob.give_raise(0.18)
    print(bob)

    for klass in [Employee, Chef, Server, PizzaRobot]:
        obj = klass(klass.__name__)
        obj.what_does()

