"""Определить класс “Матрица” со свойствами: размерность матрицы, элементы матрицы, - и методами:
вывод матрицы на экран, вычисление определителя матрицы (для матриц с размерностью 2 или 3) и проверки,
является ли матрица единичной, нулевой или диагональной.
"""


class matrix():
    array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    N = 3
    M = 3

    def print(self):
        print("MATRIX:")
        for i in range(0, len(self.array)):
            for j in range(0, len(self.array[i])):
                print(self.array[i][j], end=' | ')
            print()

    def determinant(self):
        arr = self.array
        if len(arr) == 2:
            determatrix = arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1]
            print("Данная матрица имеет размерность 2х2.")
            print(f"Определитель для матрицы равен {determatrix}")
        elif len(arr) == 3:
            determatrix = arr[0][0]*arr[1][1]*arr[2][2] + arr[0][1]*arr[1][2]*arr[2][0] + arr[0][2]*arr[1][0]*arr[2][1]\
                          - arr[0][2]*arr[1][1]*arr[2][0] - arr[0][0]*arr[1][2]*arr[2][1] - arr[0][1]*arr[1][0]*arr[2][2]
            print(f"Определитель для матрицы равен {determatrix}")
        else:
            print("Параметры данной матрицы не подходят для определения определителя")

    def propertiesmatrix(self):
        #
        pass

    def identitymatrix(self):
        arr = self.array
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if i == j:
                    if arr[i][j] != 1:
                        flag = False
                if i != j:
                    if arr[i][j] != 0:
                        flag = False
        return print(flag)

    def nullmatrix(self):
        arr = self.array
        flag = True
        for i in range(0, len(arr)):
            for j in range(0, len(arr[i])):
                if arr[i][j] != 0:
                    flag = False
        return print(flag)


matrix().print()
matrix().determinant()
matrix().identitymatrix()
matrix().nullmatrix()