"""Дан диапазон чисел от 1 до 9. Написать программу которая будет последовательно суммировать числа из
 диапазона, пока не будет достигнута сумма
равная 15 и затем выведет на кран количество чисел, которые для этого потребовалось сложить.
 Написать два варианта решения задачи с ипользованием цикла For и while"""
summa = 0
index = 0
for i in range(1, 9):
    index += 1
    summa += i
    if summa == 15:
        print(summa)
        print(index)
