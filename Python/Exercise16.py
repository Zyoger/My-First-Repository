pas = input("Введите пароль ")
con1 = len(pas) >= 5
con2 = not pas.isupper() and not pas.islower()
con3 = bool(set(pas) & {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'})
con4 = bool(set(pas) & {'@', '#', '%', "&"})
# print(set(pas) & {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'})
# print(con1, con2, con3, con4)
if (con1 + con2 + con3 + con4) >= 3:
    print('Password accept')
else:
    print('Password wrong')

