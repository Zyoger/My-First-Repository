A = 0   # Саша
B = 0   # Ваня
C = 1   # Коля

f1 = B and not A and not C
f2 = C and not A and not B
f3 = not B and (A or C)
f4 = (f1 and f2 and not f3) or (f1 and not f2 and f3) or (not f1 and f2 and f3)

print('Вазу разбил', f4)

