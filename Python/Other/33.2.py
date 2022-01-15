"""Дана последовательность целых чисел. Найти в каждом числе сумму четных цифр"""

l = [1010110, 22, 40, 123456789, 50, 666, 78, 84848, 81, 246810]


def sum_of_even_digits(x):
    """Функция находит сумму четных цифр в числе. Возвращает сумму или (Четныйх цифр в числе нет)"""
    sum_number = 0
    for i in range(len(str(x))):
        number = x % 10
        if number % 2 == 0:
            sum_number += number
            x //= 10
        else:
            x //= 10
    return sum_number


for elem in l:
    print("Для числа", elem, "сумма его четных цифр равна", sum_of_even_digits(elem))
