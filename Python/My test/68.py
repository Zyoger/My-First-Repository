dayInMonth = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]


def summYear(year):
    summ = year // 100 + year % 100
    return summ


for year in range(1940, 2050):
    for month in range(0, 12):
        for day in range(1, dayInMonth[month] + 1):
            allsumm = summYear(year) + (month + 1) + day
            if (allsumm == 68):
                print(year, month + 1, day, sep=".", end=" - ")
                print('68')


