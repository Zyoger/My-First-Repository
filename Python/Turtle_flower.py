def rend_circle(r, n):
    import turtle
    from random import random
    from math import sin, radians
    turtle.pensize(5)
    a = 8  # Угол поворота (скорость отрисовки)
    N = int(360 / a)
    step = 2 * r * sin(radians(a / 2))
    turtle.shape('arrow')
    turtle.left(n)
    for i in range(N):
        turtle.color(random(), random(), random())  # случайный цвет линии
        turtle.left(a)
        turtle.forward(step * a)


rad = int(input("Введите радиус "))
n_flow = int(input("Введите количество окружностей "))
for c in range(n_flow):
    n = 360 / n_flow
    rend_circle(rad, n)
