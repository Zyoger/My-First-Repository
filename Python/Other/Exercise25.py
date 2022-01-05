"""⦁	Дано натуральное число N. Определить, является ли оно простым."""
n = int(input("Введите число N "))
p = True
for i in range(2, n // 2 + 1):
    if n % i == 0:
        p = False
if p == False:
    print("Не простое")
else:
    print("Простое")
