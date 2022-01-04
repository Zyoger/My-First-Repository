import turtle
from random import random
from math import sin, radians
n = int(input("Введите количество фигур "))


def rend(R, N):
    step = 2 * R * sin(radians(180/N))              # длина прямой
    print(step)
    p_deg = (180 - (360 / N)) / 2                   # угол между двух ближайших радиусов в вершины многоуголбника
    turtle.penup()
    turtle.forward(R)                               # смещение курсора на радиус многоугольника
    turtle.left(90 + (90 - p_deg))                  # значение угла поворота в начальной точке
    turtle.pendown()
    turtle.showturtle()
    turtle.color(random(), random(), random())      # случайный цвет линии
    for i in range(N):                              # цикл отрисовывающий многоугольник
        turtle.forward(step)
        turtle.left(180 - 2 * p_deg)
    turtle.penup()
    turtle.hideturtle()
    turtle.home()
    turtle.pendown()


for i in range(n):                                  # цикл количества фигур
    print(i + 3)
    rend(30 + i*15, i + 3)                          # можно скорректировать радиус и размер стороны многоугольника

turtle.exitonclick()