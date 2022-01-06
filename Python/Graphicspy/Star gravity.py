import graphics as gr
import math
import random
SIZE_X = 800  # Размер окна по ширине
SIZE_Y = SIZE_X*0.5  # Размер окна по высоте (соотношение сторон 16/9)
window = gr.GraphWin("Star", SIZE_X, SIZE_Y)
gravity_speed = -2
starting_speed = 1  # Начальная скорость планеты
starting_angle_planet = 80  # Начальное направление вектора движения планеты
t = 0

star = gr.Circle(gr.Point(SIZE_X/2, SIZE_Y/2), SIZE_X/16)  # Звезда
star.setFill('red')
star.draw(window)

x_pl = random.randint(0, SIZE_X)
y_pl = random.randint(0, int(SIZE_Y))

planet = gr.Circle(gr.Point(x_pl, y_pl), SIZE_X/128)  # Планета
planet.setFill('blue')
planet.draw(window)


while True:
    # Мне нужно переписать вычисление dist_between_objects, angle_x, angle_y в зависимости от текущих координат
    # планеты. Попробовать это реализовать через функцию которая прибавляет к начальным координатам координаты сдвига,
    # по аналогии с примером из задания.
    dist_between_objects = math.sqrt(
        (SIZE_X / 2 - x_pl) ** 2 + (SIZE_Y / 2 - y_pl) ** 2)  # Расчет расстояния между объектами
    print(dist_between_objects)

    angle_x = math.asin((SIZE_Y / 2 - y_pl) / dist_between_objects) / math.pi * 180
    print('Угол от оси Х', angle_x)

    angle_y = math.asin((SIZE_X / 2 - x_pl) / dist_between_objects) / math.pi * 180
    print('Угол от оси Y', angle_y)

    if angle_x > 0 and angle_y > 0:
        angle = 270 + angle_x - 180
        print("Абсолютный угол 1 =", angle)
    elif angle_x > 0 and angle_y < 0:
        angle = 180 + angle_x
        print("Абсолютный угол 2 =", angle)
    elif angle_x < 0 and angle_y < 0:
        angle = 360 + angle_y
        print("Абсолютный угол 3 =", angle)
    elif angle_x < 0 and angle_y > 0:
        angle = angle_y
        print("Абсолютный угол 4 =", angle)

    gravity_vector = gravity_speed + starting_speed - 2*gravity_speed*starting_speed*\
                     math.cos(math.radians(angle - starting_angle_planet))
    speed_x = gravity_vector*math.cos(math.radians(angle_x))
    speed_y = gravity_vector * math.sin(math.radians(angle_y))
    print(gravity_vector)
    planet.move(speed_x, speed_y)
    gr.time.sleep(0.02)

