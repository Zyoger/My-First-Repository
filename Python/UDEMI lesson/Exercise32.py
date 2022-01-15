m = [[1, 2, 2, 4, 6], [6, 7, 3, 8, 4], [9, 6, 4, -20, 0], [4, 6, 1, 8, 3], [5, 80, 9, 4, 2]]
max_elem = m[0][0]
min_elem = m[0][0]
i_max = j_max = i_min = j_min = 0
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        if m[i][j] > max_elem:
            max_elem = m[i][j]
            i_max = i
            j_max = j
        elif m[i][j] < min_elem:
            min_elem = m[i][j]
            i_min = i
            j_min = j
m[i_max][j_max], m[i_min][j_min] = m[i_min][j_min], m[i_max][j_max]
print('Максимальный элемент =', max_elem, ", позиция элемента ", i_max, j_max)
print('Минимальный элемент =', min_elem, ", позиция элемента ", i_min, j_min)
print("Матрица с замененными элементами", m)