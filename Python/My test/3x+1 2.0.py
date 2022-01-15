x = 100000
for i in range(1, x):
    i += 3
    ix = i
    it = 0
    while i != 1:
        if i % 2 == 0:
            i /= 2
            it += 1
        else:
            i = i*3 + 1
            it += 1
    print("Число", ix, "совершает", it, "итераций")


# 295147905179352825856