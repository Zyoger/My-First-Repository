def genegate_numbers(N:int, M:int, prefix=None):
    if M == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        genegate_numbers(N, M-1, prefix)
        prefix.pop()


genegate_numbers(11, 2)
