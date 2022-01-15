"""Дан диапазон целых чисел от n1 до n2. Найти факториал каждого третьего простого числа в заданном диапазоне. """

l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

def factorial(x):
    """Функция находит факториал числа. Возвращает факториал"""
    f = 1
    for i in range(2, x + 1):
        f *= i
    return f

def simple_number(x):
    """Функция проверят является ли число простым. Возвращает True или False"""
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True


flag = 0
for elem in l:
    if simple_number(elem):
        flag += 1
    if flag == 3:
        print(factorial(elem))
        flag = 0
