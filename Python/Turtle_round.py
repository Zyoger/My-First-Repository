import turtle
from math import sin, radians
r = int(input("Введите радиус "))
a = 4                               # Угол поворота
N = int(360 / a)
step = 2 * r * sin(radians(a / 2))
turtle.shape('arrow')
turtle.penup()
turtle.forward(r)
turtle.left(90)
turtle.pendown()
for i in range(N):
    turtle.left(a)
    turtle.forward(step * a)
turtle.mainloop()
