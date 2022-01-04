import math

a = 10
a_rad = math.radians(a)
y = math.cos(3/8*math.pi - a_rad/4)**2 - math.cos(11/8*math.pi + a_rad/4)**2
z = math.sqrt(2)/2*math.sin(a_rad/2)
x = y - z
print('y =', y)
print('z =', z)
print('x =', x)
