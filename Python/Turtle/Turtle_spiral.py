import turtle
turtle.shape('turtle')
k = 0.2
fi_rad = 0.1
fi_deg = fi_rad * (180/3.14)
for i in range(0, 500):
    turtle.forward(k * fi_rad)
    turtle.left(fi_deg)
    fi_rad += 0.1
    