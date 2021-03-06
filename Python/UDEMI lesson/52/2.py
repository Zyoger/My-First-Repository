"""Определить класс “Матрица” со свойствами: размерность матрицы, элементы матрицы,- и методами:
вывод матрицы на экран, вычисление определителя матрицы (для матриц с размерностью 2 или 3) и проверки,
является ли матрица единичной, нулевой или диагональной.
"""
"""
Измените класс “Матрица” следующим образом:
свойства класса - размерность матрицы и элементы - должны быть динамическими и задаваться внутри нового метода,
определяющего матрицу;
добавьте статические свойства - общее количество созданных матриц, количество единичных, нулевых и диагональных матриц;
добавьте метод, реализующий форматированный вывод на экран статических свойств класса.

"""
"""Изменить классы “Прямая” и “Матрица”  следующим образом:
все статические свойства классов должны изменяться только внутри классовых методов;
выделить один или несколько вспомогательных методов (если это не было сделано ранее) и оформить их в виде статических
методов.
"""


class Matrix:
    """
    Класс матрица
    """

    # статические переменные
    number_matrix = 0
    number_diagonal_matrix = 0
    number_null_matrix = 0
    number_identity_matrix = 0

    def __new__(cls, *args, **kwargs):
        print("--This is constructor--")
        return super().__new__(cls)

    def __init__(self,  n, m, array):
        print("--This is initialization--")
        self.n = n
        self.m = m
        self.arr = array
        Matrix.set_property(Matrix.null_matrix(array), Matrix.diagonal_matrix(array), Matrix.identity_matrix(array), 1)

    def __del__(self):
        print("--This is destructor--")

    @classmethod
    def set_property(cls, a, b, c, d):
        """
        Изменяет свойства матрицы.
        :return:
        """
        cls.number_matrix += d
        if a:
            cls.number_null_matrix += 1
        if b:
            cls.number_diagonal_matrix += 1
        if c:
            cls.number_identity_matrix += 1

    def print_matrix(self):
        """
         Выводит матрицу на экран.
        """
        print(f"MATRIX {Matrix.number_matrix}:")
        arr = self.arr
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                print(arr[i][j], end=' | ')
            print()
        self.determinant()

    def determinant(self):
        """
        Вычисляет определитель матрицы.
        :return: определитель
        """
        arr = self.arr
        if len(arr) == 2:
            determinant_matrix = arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]
            print("Данная матрица имеет размерность 2х2.")
            print(f"Определитель для матрицы равен: {determinant_matrix}")
        elif len(arr) == 3:
            determinant_matrix = arr[0][0] * arr[1][1] * arr[2][2] + arr[0][1] * arr[1][2] * arr[2][0] \
                               + arr[0][2] * arr[1][0] * arr[2][1] - arr[0][2] * arr[1][1] * arr[2][0] \
                               - arr[0][0] * arr[1][2] * arr[2][1] - arr[0][1] * arr[1][0] * arr[2][2]
            print("Данная матрица имеет размерность 3х3.")
            print(f"Определитель для матрицы равен: {determinant_matrix}")
        else:
            print("Параметры данной матрицы не подходят для определения определителя.")

    @staticmethod
    def identity_matrix(arr):
        """
        Функция определяет, является ли матрица единичной.
        :return: True если матрица единичная.
        """
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if i == j:
                    if arr[i][j] != 1:
                        flag = False
                if i != j:
                    if arr[i][j] != 0:
                        flag = False
        return flag

    @staticmethod
    def null_matrix(arr):
        """
        Функция определяет, является ли матрица нулевой.
        :return: True если матрица нулевая.
        """
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if arr[i][j] != 0:
                    flag = False
        return flag

    @staticmethod
    def diagonal_matrix(arr):
        """
        Функция определяет, является ли матрица диагональной.
        :return: True если матрица диагональная.
        """
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if i == j:
                    if arr[i][j] == 0:
                        flag = False
                if i != j:
                    if arr[i][j] != 0:
                        flag = False
        return flag


print()

print("*"*60)
arr1 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
m1 = Matrix(3, 3, arr1)
m1.print_matrix()

print("*"*60)
arr2 = [[0, 0], [0, 0]]
m2 = Matrix(2, 2, arr2)
m2.print_matrix()

print("*"*60)
arr3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m3 = Matrix(3, 3, arr3)
m3.print_matrix()

print("="*60)
print("\tКоличество созданных матриц: ", Matrix.number_matrix)
print("\tКоличество диагональных матриц: ", Matrix.number_diagonal_matrix)
print("\tКоличество нулевых матриц: ", Matrix.number_null_matrix)
print("\tКоличество единичных матриц: ", Matrix.number_identity_matrix)
print("="*60)
