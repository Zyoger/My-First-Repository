import math
a = 1
b = 5
c = -9

d = b * b - 4 * a * c

if b < 0:
    print("Корней нет")
else:
    y1 = (-b + math.sqrt(d)) / 2 * a
    y2 = (-b - math.sqrt(d)) / 2 * a
    if y1 < 0 and y2 < 0:
        print("Корней нет")
    elif y1 >= 0 and y2 >= 0:
        x1 = math.sqrt(y1)
        x2 = -x1
        x3 = math.sqrt(y2)
        x4 = -x3
        print("Корни равны", x1, x2, x3, x4)
    elif y1 >= 0:
        x1 = math.sqrt(y1)
        x2 = -x1
        print("Корни равны", x1, x2)
    else:
        x1 = math.sqrt(y2)
        x2 = -x1
        print("Корни равны", x1, x2)
