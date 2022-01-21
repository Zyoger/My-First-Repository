"""⦁	Написать рекурсивную функцию подсчета суммы элементов списка чисел."""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sum_number(x):
    if len(x) == 0:
        return 0
    else:
        return x[0] + sum_number(x[1:])


print(sum_number(l))