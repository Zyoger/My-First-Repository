"""Написать функцию, которая принимает строку с разделенными дефисом словами и возвращает эту же строку со словами
 отсортированными в алфавитном порядке. Например, строка “green-red-yellow-black-white” должна быть преобразована в
  строку “black-green-red-white-yellow”."""

line = 'green-red-yellow-black-white'


def sort(in_line):
    new_line = in_line.split('-')
    new_line = sorted(new_line)
    new_line = "-".join(new_line)
    return new_line


print(line)
print(sort(line))
