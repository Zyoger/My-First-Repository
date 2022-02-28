"""Создать класс “Четырехугольник”, свойства - координаты 4-х точек. Предусмотреть в классе методы проверки
 существования четырехугольника*, вычисления и вывода сведений о фигуре - длины сторон, диагонали, периметр, площадь.
  Создать производный класс “Параллелограмм”. Предусмотреть в классе проверку, является ли фигура параллелограммом**.
    Написать программу, демонстрирующую работу с классом: дано N четырехугольников и M параллелограммов, найти среднюю
    площадь N четырехугольников и параллелограммы с наименьшей и наибольшей площадями."""
from math import sqrt


class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def exist(self):
        arr = Quadrilateral.calc_side(self)
        if (arr[0] < (arr[1] + arr[2] + arr[3])) and (arr[1] < (arr[0] + arr[2] + arr[3]))\
                and (arr[2] < (arr[1] + arr[0] + arr[3])) and (arr[3] < (arr[1] + arr[2] + arr[0])):
            return True
        return False

    def calc_side(self):
        ab = sqrt((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2)
        bc = sqrt((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2)
        cd = sqrt((self.c[0] - self.d[0]) ** 2 + (self.c[1] - self.d[1]) ** 2)
        da = sqrt((self.d[0] - self.a[0]) ** 2 + (self.d[1] - self.a[1]) ** 2)
        return ab, bc, cd, da

    def calc_diagonal(self):
        l = sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        m = sqrt((self.b[0] - self.d[0]) ** 2 + (self.b[1] - self.d[1]) ** 2)
        return l, m

    def print(self):
        pass


a = Quadrilateral([2, 2], [3, 8], [8, 7], [8, 2])
print(a.calc_side())
print(a.calc_diagonal())
print(a.exist())
