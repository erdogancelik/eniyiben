""" A Garage Full of Classy Vehicles"""

class Vehicle(): # Base Vehicle class

    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4 # a full tank of gas

    def drive(self):
        if self.gas >0:
            self.gas -=1
            print('The {} {} goes Vroom!'.format(self.color, self.manufacturer))
        else:
            print('The {} {} sputters out of gas.'.format(self.color, self.manufacturer))

class Car(Vehicle): # Inherits from Vehicle class

    # turn the radio on
    def radio(self):
        print("Rockin' Tunes")

    # open the window
    def window(self):
        print("Ahh.. fresh air!")


class Motorcycle(Vehicle): # Inherits from Vehicle class

    # put on motorcycle helmet
    def helmet(self):
        print('Nice and safe!')

    def add_gas(self, amount):
        self.gas = self.gas + amount

class ECar(Car):

    def drive(self):
        self.gas = None
        print('The {} {} goes ssshhhh!'.format(self.color, self.manufacturer))


my_car = Car('black', 'Subaru')
my_mc = Motorcycle('orange', 'Yamaha')

my_car.drive()

print(my_car.gas)

my_mc.drive()

print(my_mc.gas)

my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.drive()
my_mc.add_gas(2)

print(my_mc.gas)

prius = ECar('white', 'Toyota')
prius.drive()
prius.window()
prius.radio()
print(prius.gas)


