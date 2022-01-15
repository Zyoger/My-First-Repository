def render_star(number, radius):
    """Данная функция отрисовывает звезду с N количеством лучей (от 5 до ...)
    N - целое натуральное число
    R - радиус отрисовки звезды
    """
    import turtle
    from math import sin, radians
    polygon_side = 2 * radius * sin(radians(180 / number))              # Расчет вспомогательного отрезка
    angle = (180 - (360 / number)) / 2                                  # Расчет вспомогательного угла
    step = 2 * polygon_side * sin(radians(angle))                   # Расчет смещения черепахи
    angle_start = (180 - (2 * (360 / number))) / 2                  # Угол начального отклонения
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(180 - angle_start)
    turtle.pendown()
    for i in range(number):
        if number > 5:
            turtle.forward(step)
            turtle. left(180 - angle_start + 90 / number)                   # для более 5 лучей
        else:
            turtle.forward(step)
            turtle. left(180 - angle_start * 2)                               # для 5 лучей и меньше
    turtle.exitonclick()


render_star(int(input("Ведите количесво лучей ")), int(input("Введите радиус ")))
print("WORK")

