"""⦁	Отредактируйте решение задачи о паролях из контрольной работы таким образом, чтобы программа после выполнения
 всех проверок выводила бы на экран сообщение о том, является ли пароль безопасным.  Критерии безопасности пароля:
⦁	длина пароля не менее 5 символов
⦁	содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре: A-Z, a-z
⦁	содержит цифры от 0 до 9
⦁	содержит хотя бы один из символов: @, #, %, &
"""

pas = input()
con1 = len(pas) >= 5
con2 = not pas.isupper() and not pas.islower()
con3 = set(pas) & {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
con4 = set(pas) & {'@', '#', '%', "&"}
if con1 and con2 and con3 and con4:
    print('Password accept')
else:
    print('Password wrong')

