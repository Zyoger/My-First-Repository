import turtle

A0 = (3, 4, 6, 1, 7)
A1 = (2, 4, 5, 6, 7)
A2 = (2, 3, 4, 5, 1, 6)
A3 = (2, 3, 4, 2, 5, 1)
A4 = (2, 3, 2, 5, 4, 5, 6)
A5 = (2, 3, 4, 3, 2, 5, 6, 1)
A6 = (2, 3, 4, 3, 2, 1, 6, 5, 2)
A7 = (2, 3, 4, 5, 1)
A8 = (2, 3, 4, 5, 6, 1, 2, 5)
A9 = (2, 5, 2, 3, 4, 5, 6, 1)

a = 30  # Размер символа


def draw(xy):
    x = turtle.xcor()
    y = turtle.ycor()
    if xy == 1:
        turtle.goto(x, y)
    elif xy == 2:
        turtle.goto(x, y + a)
    elif xy == 3:
        turtle.goto(x, y + a*2)
    elif xy == 4:
        turtle.goto(x + a, y + a*2)
    elif xy == 5:
        turtle.goto(x + a, y - a)
    elif xy == 6:
        turtle.goto(x + a, y)
    elif xy == 7:
        turtle.goto(x + a*2, y)


def move(xy):
    pass

"""
def start():
    turtle.goto(a * 2, 0)
"""

index = int(str(input("Введите индекс "))[::-1])
print("Развернутый индекс ", index)

for i in range(len(str(index))):
    if index % 10 == 0:
        for i in A0:
            draw(i)
        index //= 10
    if index % 10 == 1:
        for i in A1:
            draw(i)
        index //= 10
    if index % 10 == 2:
        for i in A2:
            draw(i)
        index //= 10
    if index % 10 == 3:
        for i in A3:
            draw(i)
        index //= 10
    if index % 10 == 4:
        for i in A4:
            draw(i)
        index //= 10
    if index % 10 == 5:
        for i in A5:
            draw(i)
        index //= 10
    if index % 10 == 6:
        for i in A6:
            draw(i)
        index //= 10
    if index % 10 == 7:
        for i in A7:
            draw(i)
        index //= 10
    if index % 10 == 8:
        for i in A8:
            draw(i)
        index //= 10
    if index % 10 == 9:
        for i in A9:
            draw(i)
        index //= 10
