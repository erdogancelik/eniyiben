from Designing_w_Classes.Inheritance import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for pizza to', server)

class Oven:
    def bake(self):
        print('Oven is baking')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.what_does()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('.....')
    scene.order('Shaggy')


