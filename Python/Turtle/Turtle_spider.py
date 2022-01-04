import turtle
n = 12          # Количество лучей
a = 360 / n     # Вычисление угла
l = 100         # Длина лучей
for i in range(1, n + 1):
    turtle.forward(l)
    turtle.stamp()
    turtle.forward(-l)
    turtle.right(a)
