"""Выведите на экран все числа в интервале от 0 до 6 включительно, кроме чисел 3 и 5."""

a = 0
while a <= 6:
    if a != 3:
        if a != 5:
            print(a)
            a += 1
        else:
            a += 1
    else:
        a += 1
else:
    print("Задача завершена")