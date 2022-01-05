p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s = 0
for n in p:
    k = 0
    for i in range(1, n + 1):
        if n % i == 0:
            k += 1
    if k == 2:
        s += 1
print(s)
