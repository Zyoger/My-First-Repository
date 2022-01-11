m = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
flag = True
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        if i == j:
            if m[i][j] != 1:
                flag = False
                break
        else:
            if m[i][j] != 0:
                flag = False
                break
if flag:
    print("Матрица единичная")
else:
    print('Матрица не единичная')