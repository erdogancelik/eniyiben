class Life:
    def __init__(self, name):
        self.name = name

    def live(self):
        print('Happy ' + self.name)

    def __del__(self):
        print('Bye ' + self.name)


Brian = Life('Brian')
Brian.live()
Brian = ' end'