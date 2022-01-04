import turtle

a = 30  # Size number
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()


def DrawIndex (number):
    """Функция отрисовки числа
    """
    x, y = turtle.pos()
    if number == 0:
        turtle.goto(x, y + a*2)
        turtle.goto(x + a, y + a*2)
        turtle.goto(x + a, y)
        turtle.goto(x, y)
        turtle.penup()
        turtle.goto(x + a*2, y)
        turtle.pendown()
    if number == 1:
        turtle.penup()
        turtle.goto(x, y + a)
        turtle.pendown()
        turtle.goto(x + a, y + a*2)
        turtle.goto(x +a, y)
        turtle.penup()
        turtle.goto(x + a*2, y)
        turtle.pendown()
    if number == 2:
        turtle.penup()
        turtle.goto(x, y + a*2)
        turtle.pendown()
        turtle.goto(x + a, y + a*2)
        turtle.goto(x + a, y + a)
        turtle.goto(x, y)
        turtle.goto(x + a, y)
        turtle.penup()
        turtle.goto(x + a*2, y)
        turtle.pendown()
    if number == 3:
        turtle.penup()
        turtle.goto(x, y + a*2)
        turtle.pendown()
        turtle.goto(x + a, y + a*2)
        turtle.goto(x, y + a)
        turtle.goto(x + a, y + a)
        turtle.goto(x, y)
        turtle.penup()
        turtle.goto(x + a*2, y)
        turtle.pendown()
    if number == 4:
        turtle.penup()
        turtle.goto(x, y + a*2)
        turtle.pendown()
        turtle.goto(x, y + a)
        turtle.goto(x + a, y + a)
        turtle.goto(x + a, y)
        turtle.goto(x + a, y + a*2)
        turtle.penup()
        turtle.goto(x + a * 2, y)
        turtle.pendown()
    if number == 5:
        turtle.goto(x + a, y)
        turtle.goto(x + a, y + a)
        turtle.goto(x, y + a)
        turtle.goto(x, y + a*2)
        turtle.goto(x + a, y + a*2)
        turtle.penup()
        turtle.goto(x + a * 2, y)
        turtle.pendown()


index = int(input("Введите индекс "))

mirror_index = int(str(index)[::-1])  # Не работает если в начале стоит 0

"""def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r"""

for i in range(6):
    DrawIndex(mirror_index % 10)
    mirror_index = mirror_index // 10
