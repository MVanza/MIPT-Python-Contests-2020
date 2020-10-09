class Car:
    def __init__(self, c, s, n):
        self.capacity = c
        self.speed = s
        self.number = n


class RaceCar(Car):
    def __init__(self, s):
        self.capacity = 0
        self.speed = s
        self.number = None
