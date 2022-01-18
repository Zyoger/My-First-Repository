"""Напишите функцию, принимающую сведения об авторе (в виде произвольного списка именованных аргументов)
и выводящая их на экран в указанном формате: И. О. Фамилия (дата рождения - дата смерти) - краткая информация
Например: А. С. Пушкин (6.06.1799 - 10.02.1837) - русский поэт, драматург и прозаик. И. Соболь (24.08.1939)
 - израильский драматург, писатель и режиссер."""


def writer(**kwargs):
    print(kwargs['name']," (", kwargs['date'], ') - ', kwargs['other'], sep="")


writer(name="А. С. Пушкин", date="6.06.1799 - 10.02.1837", other="русский поэт, драматург и прозаик.")
writer(name="И. Соболь", date="24.08.1939", other="израильский драматург, писатель и режиссер.")