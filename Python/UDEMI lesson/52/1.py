"""Определите класс “Прямая” со свойствами:  координаты двух точек (x1, y1) и (x2, y2),
- и методами: вывод уравнения прямой и  определение точек пересечения с осями координат."""

class line():
    x1 = 1
    x2 = 2
    y1 = 3
    y2 = 4


    def lineEquation (self):
        A = self.y1 - self.y2
        B = self.x2 - self.x1
        C = self.x1*self.x2 - self.x2*self.y1
        print(f'{A}x+{B}y+{C}=0')


    def intersectionPoints (self):
        pass



l = line()
l.lineEquation()
