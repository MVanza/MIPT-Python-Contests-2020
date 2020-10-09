class Garage:
    # Конструктор и деструктор, если нужны
    def __init__(self):
        self.pk = []
    # Запарковать машину v
    def park(self, v):
        self.pk.append(v)

    # Пересчитать машины заданного типа t.
    # Вернуть количество.
    def count(self, t):
        k = 0
        for i in self.pk:
            if isinstance(i, t):
                k += 1
        return k

    # Получить самую быструю машину заданного типа t.
    # Вернуть экземпляр.
    def get_fastest_of_type(self, t):
        j = None
        k = 0
        for i in self.pk:
            if isinstance(i, t):
                if k < i.speed:
                    k = i.speed
                    j = i
        return j
