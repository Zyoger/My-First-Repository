"""3.	Написать функцию, которая принимает в качестве аргумента строку и подсчитывает в ней количество символов
в верхнем и нижнем регистре."""

def up_or_down(x):
    up = 0
    down = 0
    for i in x:
        if i.isupper():
            up += 1
        else:
            down += 1
    return print("Up ", up, "Down ", down)


l = 'Написать функцию. Которая принимает в качестве аргумента строку и подсчитывает в ней количество символов' \
    ' в верхнем и нижнем регистре'

up_or_down(l)