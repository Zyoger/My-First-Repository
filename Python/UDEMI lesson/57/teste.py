"""
Создать класс “Треугольник”, свойства - длины трех сторон.
Предусмотреть в классе методы проверки существования треугольника,
вычисления и вывода сведений о фигуре - длины сторон, углы, периметр, площадь.

Создать производный класс “Равносторонний треугольник”.

Написать программу, демонстрирующую работу с классами: дано K треугольников и L равносторонних треугольников,
найти среднюю площадь для K треугольников и равносторонний треугольник с наибольшим периметром.

"""
from math import acos, degrees, sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_triangle(self):
        return f'\u25b3ABC ({self.a}, {self.b}, {self.c})'

    def exists(self):
        if (self.a + self.b > self.c) \
                and (self.a + self.c > self.b) \
                and (self.b + self.c > self.a):
            print(f'{self.get_triangle()} exists.')
            return True

        print(f'{self.get_triangle()} does not exist.')
        return False

    def get_sides(self):
        print(f'Sides: {self.a}, {self.b}, {self.c}')
        return self.a, self.b, self.c

    def get_angles(self):
        ac = acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))
        ab = acos((self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b))
        cb = acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))

        print(f'\u2220CAB: {ac:.2f} Rad, {degrees(ac):.2f} Grad')
        print(f'\u2220ABC: {ab:.2f} Rad, {degrees(ab):.2f} Grad')
        print(f'\u2220BCA: {cb:.2f} Rad, {degrees(cb):.2f} Grad')

        return ac, ab, cb

    def get_perimeter(self, to_print=True):
        p = self.a + self.b + self.c
        if to_print:
            print(f'Perimeter: {p}')
        return p

    def get_square(self):
        p = self.get_perimeter(to_print=False) / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print(f'Square: {s:.2f}')
        return s


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


tr = [Triangle(2, 5, 6), Triangle(5, 2, 4), Triangle(7, 3, 6)]
eq_tr = [EquilateralTriangle(5), EquilateralTriangle(8), EquilateralTriangle(6), EquilateralTriangle(4)]

# print(tr[0].get_triangle())
# tr[0].exists()
# tr[0].get_sides()
# tr[0].get_angles()
# tr[0].get_perimeter()
# tr[0].get_square()

tr_s = list(map(lambda tr: tr.get_square(), tr))
tr_s_avg = sum(tr_s) / len(tr_s)

eq_tr_max_p = max(eq_tr, key=lambda tr: tr.get_perimeter())

print('*'*50)
print(f'The average triangles square: {tr_s_avg:.2f}')
print(f'The equilateral triangle with the max perimeter: {eq_tr_max_p.get_triangle()}')
