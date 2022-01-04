import turtle
turtle.left(90)


def rend_circle(r):
    import turtle
    from random import random
    from math import sin, radians
    turtle.pensize(3)
    a = 4  # Угол поворота (скорость отрисовки)
    N = int(360 / a)
    step = 2 * r * sin(radians(a / 2))
    turtle.shape('arrow')
    for i in range(N):
        # turtle.color(random(), random(), random())  # случайный цвет линии
        turtle.left(a)
        turtle.forward(step * a)


rad = int(input("Введите радиус "))
n_flow = int(input("Введите количество окружностей "))
for c in range(n_flow):
    rend_circle(rad)
    rend_circle(-rad)
    rad += 2

