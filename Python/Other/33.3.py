"""Дана последовательность целых чисел. Для каждого числа последовательности проверить,
 представляют ли его цифры строго возрастающую последовательность."""

l = [123, 321, 456, 1357, 5555, 876543]


def ascending_sequence(number):
    """Функция определяет является ли цифры числа строгой последовательностью. Возвращает True или False"""
    m = list(str(number))
    for i in range(len(l)):
        if m[i] < m[i + 1]:
            return True
        else:
            return False


for i in l:
    if ascending_sequence(i):
        print("Цифры числа", i, "являются строгой последовательностью")
    else:
        print("Цифры числа", i, "НЕ являются строгой последовательностью")