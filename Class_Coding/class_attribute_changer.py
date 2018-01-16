
class Isim:

    def __init__(self, name):
        self.name = name

    def name_changer(self, x):
        self.name = x
        return self.name

I = Isim('erdogan')
print(I.name)
print(I.name_changer('jalpa'))
