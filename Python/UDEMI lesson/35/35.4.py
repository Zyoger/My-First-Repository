"""4.	Напишите программу, которая будет складывать соответствующие элементы заданных списков чисел с помощью функции map и lambda-функции.
Например: для списков [1, 2, 3] и [4, 5, 6] результатом будет [5, 7, 9]."""

l1 = [1, 2, 3]
l2 = [4, 5, 6]


def summ(x, y):
    l3= list(map(lambda i, n: i + n, x, y))
    return print(l3)


summ(l1, l2)