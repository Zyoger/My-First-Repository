"""В файле nums.txt хранятся вещественные числа. Дописать в файл эти же числа, упорядочив их по возрастанию.
"""

with open('nums.txt', 'r+') as f:
    s = f.read()  # получаем строку
    new_s = sorted(list(map(float, s.split())))  # преобразуем в список, сортируем
    new_s = ' '.join(list(map(str, new_s)))  # список преобр. в строку
    f.write(f'\n{new_s}')  # записываем на следующую строчку