"""В файле matrix.txt построчно хранится матрица целых чисел A(n,n). Найти два наибольших простых числа.
Первое из них заменить минимальным элементом матрицы, а второе - максимальным элементом. Записать полученную матрицу в
файл result.txt.
"""
m = []
with open('matrix.txt', 'r') as f:
    for num in f.readlines():
        m.append(list(map(int, num.split())))
print(m)


def prime_number(x):
    """Возвращает True если число простое"""
    flag = True
    if x <= 1:
        return not flag
    elif x == 2:
        return flag
    else:
        for i in range(2, x):
            if x % i == 0:
                return not flag
            return flag


def min_max_elem(x):
    """Возвращает два списка с координатами максимального и минимального числа"""
    min = x[0][0]
    max = x[0][0]
    i_index_max = 0
    j_index_max = 0
    i_index_min = 0
    j_index_min = 0
    i = 0
    for row in m:
        i += 1
        j = 0
        for elem in row:
            j += 1
            if elem >= max:
                max = elem
                i_index_max = i
                j_index_max = j
            elif elem <= min:
                min = elem
                i_index_min = i
                j_index_min = j
    max_index = [i_index_max, j_index_max]
    min_index = [i_index_min, j_index_min]
    return max_index, min_index


print(min_max_elem(m))
print(m[min_max_elem(m)[0][0]][min_max_elem(m)[0][1]])
