import turtle

Vy0 = 30  # Начальная скорость по вертикали
Vx = 10   # Начальная скорость по горизонту
Vyg = 30  # Скорость падения
g = 9.8   # Ускорение свободного падения
t = 0     # Начальное время
tx = 0
x0 = -300  # Начальная координата по х
y0 = 0.01     # Начальная координата по y

while True:
    y = y0 + Vy0*t - (g * t**2)/2
    x = x0 + Vx * tx
   # v = Vyg - g*t
    turtle.goto(x, y)
    t += 0.05
    tx += 0.05
    if turtle.ycor() <= 0:
        Vy0 = Vy0 - g*t
        t = 0