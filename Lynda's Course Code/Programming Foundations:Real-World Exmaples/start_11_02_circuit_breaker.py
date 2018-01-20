""" Overloading a Circuit Breaker """

class CircuitBraker:

    def __init__(self, max_amps):
        self.capacity = max_amps
        self.load = 0

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception('connection will exceed')
        elif self.load + amps < 0:
            raise Exception("Can't be negative")
        else:
            self.load += amps


cb = CircuitBraker(20)
