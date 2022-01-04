from random import random, randint


def TurtleMove (step, angle, side):
    import turtle
    if side >= 0.5:
        turtle.left(angle)
    else:
        turtle.right(angle)
    turtle.forward(step)


for i in range(100):
    TurtleMove(randint(10, 30), randint(0, 180), random())

