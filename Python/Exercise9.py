# Дан список из 10 элементов. Удалить все элементы, расположенные справа от элемента, следующего за максимальным
s = [2, 300, 67, 34, 22, 3, 7, 80, 32, 2]

s_max = max(s)

print('Максимальное число ', s_max)

index_max = s.index(s_max)

print('Номер максимального числа ', index_max+1)

del s[index_max+2: len(s)]

print(s)

