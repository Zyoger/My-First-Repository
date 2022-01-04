import turtle
turtle.left(91)

def rend_circle(r):

    from random import random
    from math import sin, radians
    turtle.pensize(3)
    a = 4                               # Угол поворота (скорость отрисовки)
    N = int(180 / a)                    # при 360 окружность, при 180 дуга
    step = 2 * r * sin(radians(a / 2))
    turtle.shape('arrow')
    for i in range(N):
        turtle.color(random(), random(), random())  # случайный цвет линии
        turtle.right(a)
        turtle.forward(step * a)


rad = int(input("Введите радиус "))
n_flow = int(input("Введите количество окружностей "))
for c in range(n_flow):
    rend_circle(rad)
    rend_circle(rad / 3)

turtle.exitonclick()

