import graphics as gr
import math
import random
SIZE_X = 800  # Размер окна по ширине
SIZE_Y = int(SIZE_X*0.5)  # Размер окна по высоте (соотношение сторон 16/9)
window = gr.GraphWin("Star", SIZE_X, SIZE_Y)
gravity_speed = 30
starting_speed = 2  # Начальная скорость планеты
starting_angle_planet = 100  # Начальное направление вектора движения планеты
t = 0

x_st = SIZE_X/2  #  Координаты звезды
y_st = SIZE_Y/2
star = gr.Circle(gr.Point(x_st, y_st), SIZE_X/16)  # Звезда
star.setFill('red')
star.draw(window)

x_pl0 = 0
y_pl0 = 0
x_pl = random.randint(0, SIZE_X)  #  Случайные координаты планеты
y_pl = random.randint(0, SIZE_Y)
planet = gr.Circle(gr.Point(x_pl, y_pl), SIZE_X/128)  # Планета
planet.setFill('blue')
planet.draw(window)


while True:
    dist_between_objects = math.sqrt(
        (x_st - x_pl) ** 2 + (y_st - y_pl) ** 2)  # Расчет расстояния между объектами
    print("Расстояние между объектами", dist_between_objects)
    angle_x = math.asin((y_st - y_pl) / dist_between_objects) / math.pi * 180
#    print('Угол от оси Х', angle_x)     # Угол от оси Х
    angle_y = math.asin((x_st - x_pl) / dist_between_objects) / math.pi * 180
#    print('Угол от оси Y', angle_y)     # Угол от оси Y

    if angle_x > 0 and angle_y > 0:
        angle = 270 + angle_x - 180
#        print("Абсолютный угол 1 =", angle)
    elif angle_x > 0 and angle_y < 0:
        angle = 180 + angle_x
#        print("Абсолютный угол 2 =", angle)
    elif angle_x < 0 and angle_y < 0:
        angle = 360 + angle_y
#        print("Абсолютный угол 3 =", angle)
    elif angle_x < 0 and angle_y > 0:
        angle = angle_y
#        print("Абсолютный угол 4 =", angle)
    print("Направление гравитации =", angle)

    gravity_vector = gravity_speed + starting_speed - 2*gravity_speed*starting_speed*\
                     math.cos(math.radians(angle - starting_angle_planet))
    print("Угол к звезде =", angle - starting_angle_planet)
    # Скорее всего не правильно вычисляется угол, так как у меня 4 сектора
    speed_x = gravity_vector*math.cos(math.radians(angle - starting_angle_planet))
    speed_y = gravity_vector * math.sin(math.radians(angle - starting_angle_planet))
    planet.move(speed_x, speed_y)
    x_pl += speed_x
    y_pl += speed_y
    gr.time.sleep(1)

