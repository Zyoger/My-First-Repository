import turtle
n = 30
l = 10
turtle.left(-90)
for i in range(n):
    turtle.forward(l * i)
    turtle.left(90)
turtle.mainloop()