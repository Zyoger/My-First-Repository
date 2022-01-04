import turtle
from random import random, randint
number_of_molekula = 50     # Количество молекул

pool = [turtle.Turtle(shape='circle') for i in range(number_of_molekula)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))
    if random() >= 0.5:
        unit.left(randint(0, 180))
    else:
        unit.right(randint(0, 180))
for i in range(50):
    for unit in pool:
        unit.forward(randint(10, 30))
#  Исправить что бы молекула отскакивала от границы
