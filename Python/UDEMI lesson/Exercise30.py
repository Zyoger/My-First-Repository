"""Вывести на экра строку хелло наме, для всех имен длиной не более 4х символов. При этом все имена
за именем с буквой х должны быть проигнорированы"""
list = ["Rose", "Nina", "Phillip", "Alex", "Jimmy", "Max"]
for i in list:
    if len(i) > 4:
        continue
    if i.find("x") == -1:
        print("Hello,", i)
    else:
        break


