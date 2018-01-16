x = 1

class Kapsam:

    x = 2

    def global_x(self):
        print(x)

    def sinif_x(self):
        print(self.x)

    def modificated_x(self):
        self.x = 3
        print(self.x)


print(x)
I = Kapsam()
I.global_x()
I.sinif_x()
I.modificated_x()
print(I.x)


for i in Kapsam.__dict__:
    if not i.startswith('__'):
        print(i)