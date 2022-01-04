import turtle
import math
x0 = 0  # Начальные координаты
y0 = 0  # Начальные координаты
g = 9.8  # ускорение свободного падения
a = 70  # угол броска
V0 = 50  # начальная скорость
t = 0

while True:
    Vx = V0*math.cos(math.radians(a))
    Vy = V0*math.sin(math.radians(a)) - g*t
    x = x0 + Vx*t
    y = y0 + Vy*t
    t += 0.02
    if turtle.ycor() <= 0:  # Дописать условие при котором происходит отскок предмета
        Vy = -Vy
    turtle.goto(x, y)
