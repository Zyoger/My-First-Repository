# Исходный код солнечной системы
import graphics as gr

SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
coords = gr.Point(400, 700)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')
    circle.draw(window)


while True:
    draw_ball(coords)
    draw_ball.move(1, 1)
    gr.time.sleep(1)

# мув не работает для функции, нужно двигать объект драв
# и функция мув сдвигает на значение в скобках а не перемещает в данные координаты
