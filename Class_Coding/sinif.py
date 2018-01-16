class Kisi():
    def __init__(self, isim, yas, meslek, mayis):
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
        self.mayis = mayis

    def zam(self, oran):
        self.mayis = int(self.mayis * (1+oran))

class Mudur(Kisi):
    def __init__(self, isim, yas, mayis):
        Kisi.__init__(self, isim, yas, 'mudur', mayis)

    def zam(self, oran, bonus=0.1):
        Kisi.zam(self, oran + bonus)


if __name__ == '__main__':

    ali = Kisi('ali', 32, 'asker', 10000)
    ali.zam(1)
    selim = Mudur('selim',38,20000)
    selim.zam(1, 0.5)
    print(ali)
    print(selim)
