x = 1


def nester():
    x = 2
    print(x)

    class C:
        x = 3
        print(x)

        def method1(self):
            print(x)
            print(self.x)

        def method2(self):
            x = 4
            print(x)
            self.x = 5
            print(self.x)



    I = C()
    I.method1()
    I.method2()

print(x)
nester()
