"""⦁	Написать рекурсивную функцию подсчета суммы цифр положительного целого числа.
"""


def summ(x):
    if x < 0:
        x *= -1
    if x // 10 == 0:
        return x
    else:
        return x % 10 + summ(x // 10)


print(summ(15))