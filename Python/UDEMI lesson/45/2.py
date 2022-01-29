"""Создать двоичный файл nums.dat и записать в него целое число n, а затем в следующей строке n вещественных чисел.
"""

f = b'nums.dat'
n = int(input('Введите целое число: '))

with open(f, 'wb') as f:
    num = input(f'Введите {n} вещественных чисел через пробел: ')
    f.write(str(n).encode() + b'\n')
    f.write(num.encode() + b' ')
