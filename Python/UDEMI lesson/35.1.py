"""Используя функцию sorted() и lambda-функцию, отсортируйте список кортежей
 по последнему символу их второго элемента."""

l = [(1, 8, 57, 20, 25),
     (58, 20, 6, 2, 8),
     (6, 35, 87, 15, 3)]

res = sorted(l, key=lambda i: str(i[1])[-1])

print(res)
