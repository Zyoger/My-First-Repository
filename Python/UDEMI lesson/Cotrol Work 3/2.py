"""2.	Вывести на экран последовательность из первых 100 простых чисел. Найти сумму элементов полученной
 последовательности."""

count = 0
res = []


def is_prime(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True


i = 2
while count < 100:
    if is_prime(i):
        res.append(i)
        count += 1
        i += 1
    else:
        i += 1


print(res)
print(sum(res))
