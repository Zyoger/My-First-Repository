# программа для вычисления площади и длины окружности
import math

r = 10  # ведите величину радиуса окружности

s = math.pi*r**2    # расчет площади
l = 2*math.pi*r     # расчет длины окружности

print('Площадь круга = ', round(s, 3))
print('Длина окружности = ', round(l, 3))

