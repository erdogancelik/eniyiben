class Delegates:
    def delegate(self):
        self.will_call_provider()

    def will_call_provider(self):
        raise NotImplementedError('Hei')

x = Delegates()
x.delegate()