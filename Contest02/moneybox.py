class MoneyBox:
    def __init__(self):
        self.coin = 0
        self.amount = 0

    # Добавить монетку достоинством value
    def add_coin(self, value):
        self.coin += value
        self.amount += 1
    # Получить текущее количество монеток в копилке
    def get_coins_number(self):
        return self.amount
    # Получить текущее общее достоинство всех монеток
    def get_coins_value(self):
        return self.coin
