"""Написать программу, сортирующую список словарей по значению некоторого общего ключа  с помощью
 lambda-функции (например, список сотрудников по их возрасту).
"""
l = [{'Full name': 'Fedorova Elena', 'Age': 33, 'job_id': 'Manager', 'salary': 50000},
     {'Full name': 'Ivanov Konstantin', 'Age': 28, 'job_id': 'IT-Prog', 'salary': 100000},
     {'Full name': 'Glinka Margarita', 'Age': 32, 'job_id': 'ST-Clerk', 'salary': 46000}]


res = sorted(l, key=lambda x: x['Age'])

print(str(res))
