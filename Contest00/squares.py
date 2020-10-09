from math import sqrt


def is_one(n):  # тут наверное лучше бинпоиск
    return int(sqrt(n)) ** 2 == n


def is_two(n):  # по теореме Ферма-Эйлера о двух квадратах
    i = 2
    while i * i <= n:
        k = 0
        if n % i == 0:
            while n % i == 0:
                k += 1
                n = n // i
            if i % 4 == 3 and k % 2 == 1:
                return False
        i += 1
    return n % 4 != 3


def is_three(n):  # по теореме Лежандра о трёх квадратах
    while n % 4 == 0:
        n /= 4
    return n % 8 != 7


n = int(input())
if is_one(n):
    print(1)
elif is_two(n):
    print(2)
elif is_three(n):
    print(3)
else:
    print(4) 
