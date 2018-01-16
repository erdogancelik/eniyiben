""" Two Names, One Shirt"""

class Shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True



levis = Shirt()
lee = Shirt()

levis.make_dirty()
print(levis.clean)

lee.make_clean()
print(lee.clean)

