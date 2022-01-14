import turtle
turtle.hideturtle()
screen = turtle.Screen()
screen.setup(500, 900)
x = 10000
for i in range(1, x):
    i += 3
    ix = i
    it = 0
    while i != 1:
        if i % 2 == 0:
            i /= 2
            it += 1
            turtle.goto(it, i)
        else:
            i = i*3 + 1
            it += 1
            turtle.goto(it, i)
    print("Число", ix, "совершает", it, "итераций")
    turtle.clear()
    turtle.clearscreen()



# 295147905179352825856