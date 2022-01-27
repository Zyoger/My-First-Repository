"""Написать функцию, которая принимает произвольное число чисел, вычисляет их среднее арифметическое и возвращает
только те числа, которые меньше полученного среднего арифметического."""


def func(*args):
    num = []
    arithmetic_mean = sum(args)/len(args)
    for arg in args:
        if arg < arithmetic_mean:
            num.append(arg)
    return num


print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))