number = int(input("Введите число "))
Number = number
it = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
        it += 1
        print(number)
    else:
        number = number*3 + 1
        it += 1
        print(number)
print("Число", Number,"совершает", it, "итераций")
