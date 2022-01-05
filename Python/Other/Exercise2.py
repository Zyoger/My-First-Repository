print ('         Exercise 1')
"""
K   L   M   N
0   0   0   0   -
0   0   0   1   -
0   0   1   0   -
0   0   1   1   -
0   1   0   0   -
0   1   0   1   -
0   1   1   0   -
0   1   1   1   -
1   0   0   0   -
1   0   0   1   -
1   0   1   0   -
1   0   1   1   -
1   1   0   0   +
1   1   0   1
1   1   1   0
1   1   1   1

"""

K = 1
L = 1
M = 0
N = 0
f = (not K or M) or (not L or M or N)
print('f=', f)


print('         Exercise 2')

A = 1
B = 0

f1 = 0 or 1 and not (0 or 1)
f2 = 1 or 0 and 1 and 1 and 0 or 1
f3 = ((1 or 0) and (1 and 1))
f4 = ((A or 0) or B and 1) and 0

print('f1=', f1)
print('f2=', f2)
print('f3=', f3)
print('f4=', f4)


print('         Exercise 3')

x1 = 1
x2 = 0
x3 = 1
x4 = 0

f1 = (x1 or not x2) and (not x3 or x4)
f2 = (not x1 or x3) and x2 or x4
f3 = x1 and x2 or (not x3 or (x1 or x4))

print('f1=', f1)
print('f2=', f2)
print('f3=', f3)

# Ответ: 2 функция

print('         Exercise 4')

a = 1
b = 1
c = 1
d = 1
"""
a   b   c   d
0   0   0   0   +
0   0   0   1   +
0   0   1   0   +
0   0   1   1   +
0   1   0   0   -
0   1   0   1   -
0   1   1   0   -
0   1   1   1   +
1   0   0   0   -
1   0   0   1   -
1   0   1   0   -
1   0   1   1   +
1   1   0   0   +
1   1   0   1   +
1   1   1   0   +
1   1   1   1   +   
"""
f = not ((a and not b) or (not a and b)) or (c and d)
print('f=', f)
