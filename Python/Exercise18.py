"""⦁	В магазине продаются следующие товары: smart watch ($600), phone ($1000), playstation ($450), laptop ($1550),
music player ($400) и tablet ($400). Майкл хочет сделать подарок родителям. В магазине проводится акция: если он купит
товары на $1000, то любой следующий товар он получит со скидкой 30%. У Майкла есть $1300. Хватит ли у него денег, чтобы
купить музыкальный плеер маме, умные часы папе и плейстейшн себе?
sw = 600
# ph = 1000
ps = 450
# lt = 1550
mp = 400
# tb = 400
money = 1300
if  mp + sw >= 1000 and (mp + sw) + 0.7 * ps <= money \
    or ps + sw >= 1000 and (ps + sw) + 0.7 * mp <= money \
    or mp + ps >= 1000 and (mp + sw) + 0.7 * sw <= money:
    print("Денег хватает")
else:
    print("Денег не хватает")

"""
prod = {'smart watch': 600, 'phone': 1000, 'plystation': 450,
        'laptop': 1550, 'music player': 400, 'tablet': 400}

a = prod['music player']
b = prod['smart watch']
c = prod['plystation']

if a + b >= 1000 and (a + b + 0.7 * c) <= 1300 \
        or a + c >= 1000 and (a + c + 0.7 * b) <= 1300 \
        or c + b >= 1000 and (c + b + 0.7 * a) <= 1300:
    print('денег хватает')
else:
    print('денег не хватает')

