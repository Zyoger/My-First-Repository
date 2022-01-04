import math

x = 100

y = (x**2 + 2*x - 3 + (x + 1)*math.sqrt(x**2 - 9))/x**2 + 2*x - 3 + (x - 1)*math.sqrt(x**2 - 9)
z = math.sqrt((x + 3)/(x - 3))
a = y - z

print('y=', round(y, 2))
print('z=', round(z, 2))
print('a=', round(a, 2))

