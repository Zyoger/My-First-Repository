# Дан список из 10 элементов. Изменить его таким образом, чтобы все положительные элементы оказались
# в начале списка, причем, чем больше элемент, тем ближе к началу списка он должен быть

s = [6, 8, -5, -8, 54, 2, -9, 76, 43, 3]

s.sort(reverse=True)

print(s)