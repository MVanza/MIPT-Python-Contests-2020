class Car:
    def __init__(self, capacity, s, n):
        self.capacity = capacity
        self.speed = s
        self.number = n

    def __str__(self):
        return '<Car capacity:{} speed:{} number:{}>'.format(self.capacity, self.speed, self.number)
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.number == other.number
        else:
            return False
    def __hash__(self):
        return hash(self.number)
