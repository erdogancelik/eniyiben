class C1:
    def meth1(self):
        self.__X = 88

    def meth2(self):
        print(self.__X)


class C2:
    def metha(self):
        self.__X = 99

    def methb(self):
        print(self.__X)


class C3(C2, C1):
    pass

I = C3()

I.metha(); I.meth1()
print(I.__dict__)
I.methb(); I.meth2()