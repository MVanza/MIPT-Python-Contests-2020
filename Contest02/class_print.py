class Car:
    def __init__(self, capacity, s, n):
        self.capacity = capacity
        self.speed = s
        self.number = n

    def __str__(self):
        return '<Car capacity:{} speed:{} number:{}>'.format(
        self.capacity, self.speed, self.number
        )
