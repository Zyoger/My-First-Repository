"""3.	Напишите программу, которая будет считать количество четных и нечетных чисел в заданном списке с помощью lambda-функции."""
import random

l = [random.randit(1, 100)] * 10
# l = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def evenornot(x):
        even = list(map(lambda i: i % 2, x)).count(0)
        not_even = list(map(lambda i: i % 2, x)).count(1)
        return print("Четных = ", even, "не четных = ", not_even)
        
        
print(l)
evenornot(l)
