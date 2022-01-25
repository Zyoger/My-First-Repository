"""2.	Вывести на экран последовательность из первых 100 простых чисел. Найти сумму элементов полученной
 последовательности."""

# not work
def func(x):
    i = 2
    while i != x:
        p = True
        for v in range(2, i // 2 + 1):
            if i % v == 0:
                p = False
        if not p:
            return print("Не простое")
        else:
            return print(i)
    i += 1


func(100)
