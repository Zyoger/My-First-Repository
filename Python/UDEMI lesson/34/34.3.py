"""Напишите функцию, которая может принимать произвольное количество аргументов (целых чисел),
 и определять, сколько среди них двузначных и трёхзначных чисел. Определение количества разрядов
  в числе также оформить в виде отдельной функции.
"""


def number(n):
    '''Функция определяет количество разрядов в числе'''
    l = len(str(n))
    return l


def twoortree(*args):
    two = 0
    tree = 0
    for arg in args:
        if number(arg) == 2:
            two += 1
        elif number(arg) == 3:
            tree += 1
    return print('Двузначных -', two, 'Трехзначных -', tree)


twoortree(1234, 23, 43, 2, 234, 567, 234, 21)
