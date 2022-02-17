"""Определите класс “Прямая” со свойствами:  координаты двух точек (x1, y1) и (x2, y2),
- и методами: вывод уравнения прямой и  определение точек пересечения с осями координат."""

class line():
    # точка 1
    x1 = 0
    y1 = 1
    # точка 2
    x2 = 1
    y2 = 2


    def lineEquation (self):
        A = self.y1 - self.y2
        B = self.x2 - self.x1
        C = self.x1*self.x2 - self.x2*self.y1 # проверить данную формулу
        print(f'{A}x+{B}y+{C}=0')


    def intersectionPoints (self):
        x = -(self.x1*self.x2 - self.x2*self.y1)/(self.y1 - self.y2) # пересечение с Х
        y = -(self.x1*self.x2 - self.x2*self.y1)/(self.x2 - self.x1) # пересечение с Y
        print(f'Точки пересечения прямой с осями координат: ({x}:0), (0:{y})')



l = line()
l.lineEquation()
l.intersectionPoints()
