"""1.	Дана последовательность из N целых чисел. Сформировать последовательность, каждый элемент которой равен сумме
цифр соответствующего элемента исходной последовательности. Найти сумму цифр в сформированной последовательности."""

l = [19, 21, 34, 67, 89, 10, 100, 1005]


def func(x):
    """

    :param x:
    :return:
    """
    s_pos = 0
    l1 = []
    for i in x:
        s_elem = 0
        while i != 0:
            s_elem += i % 10
            i = i // 10
        else:
            l1.append(s_elem)
            s_pos += s_elem
    return print(l1, "Сумма всех элементов = ", s_pos)


print(l)
func(l)