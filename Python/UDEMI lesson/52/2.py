"""Определить класс “Матрица” со свойствами: размерность матрицы, элементы матрицы, - и методами:
вывод матрицы на экран, вычисление определителя матрицы (для матриц с размерностью 2 или 3) и проверки,
является ли матрица единичной, нулевой или диагональной.

Измените класс “Матрица” следующим образом:
свойства класса - размерность матрицы и элементы - должны быть динамическими и задаваться внутри нового метода,
определяющего матрицу;
добавьте статические свойства - общее количество созданных матриц, количество единичных, нулевых и диагональных матриц;
добавьте метод, реализующий форматированный вывод на экран статических свойств класса.

"""


class matrix():
    """
    Класс матрица
    """
    # статические переменные
    numbermatrix = 0
    diagmatrix = 0
    nulmatrix = 0
    edmatrix = 0

    def set(self, n, m, array):
        """
        Задает динамические параметры прямой.
        :return:
        """
        self.n = n
        self.m = m
        self.arr = array
        matrix.numbermatrix += 1

    def print(self):
        """
         Выводит матрицу на экран.
        """
        self.diagonalmatrix()
        self.nullmatrix()
        self.identitymatrix()
        print("*"*60)
        print("Количество созданых матриц: ", matrix.numbermatrix)
        print("Количество диагональных матриц: ", matrix.diagmatrix)
        print("Количество нулевых матриц: ", matrix.nulmatrix)
        print("Количество еденичных матриц: ", matrix.edmatrix)
        print(f"MATRIX {matrix.numbermatrix}:")
        arr = self.arr
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                print(arr[i][j], end=' | ')
            print()
        self.determinant()

    def determinant(self):
        """
        Расчитывает определитель матрицы.
        :return: определитель
        """
        arr = self.arr
        if len(arr) == 2:
            determatrix = arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1]
            print("Данная матрица имеет размерность 2х2.")
            print(f"Определитель для матрицы равен {determatrix}")
        elif len(arr) == 3:
            determatrix = arr[0][0]*arr[1][1]*arr[2][2] + arr[0][1]*arr[1][2]*arr[2][0] + arr[0][2]*arr[1][0]*arr[2][1]\
                          - arr[0][2]*arr[1][1]*arr[2][0] - arr[0][0]*arr[1][2]*arr[2][1] - arr[0][1]*arr[1][0]*arr[2][2]
            print("Данная матрица имеет размерность 3х3.")
            print(f"Определитель для матрицы равен {determatrix}")
        else:
            print("Параметры данной матрицы не подходят для определения определителя")

    def identitymatrix(self):
        """
        Функция определяет является ли матрица единичной.
        :return: True если матрица единичная.
        """
        arr = self.arr
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if i == j:
                    if arr[i][j] != 1:
                        flag = False
                if i != j:
                    if arr[i][j] != 0:
                        flag = False
        if flag:
            matrix.edmatrix += 1
        return flag

    def nullmatrix(self):
        """
        Функция определяет является ли матрица нулевой.
        :return: True если матрица нулевая.
        """
        arr = self.arr
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if arr[i][j] != 0:
                    flag = False
        if flag:
            matrix.nulmatrix += 1
        return flag

    def diagonalmatrix(self):
        """
        Функция определяет является ли матрица диагональной.
        :return: True если матрица диагональная.
        """
        arr = self.arr
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if i == j:
                    if arr[i][j] == 0:
                        flag = False
                if i != j:
                    if arr[i][j] != 0:
                        flag = False
        if flag:
            matrix.diagmatrix += 1
        return flag

    def propertiesmatrix(self):
        pass


arr1 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
m1 = matrix()
m1.set(3, 3, arr1)
m1.print()

arr2 = [[0, 0], [0, 0]]
m2 = matrix()
m2.set(2, 2, arr2)
m2.print()

arr3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m3 = matrix()
m3.set(3, 3, arr3)
m3.print()
# print(matrix().numbermatrix)
