import math

credit_for = {'本 金(元)': 0, '利 息(元)': 0, '本金利息累計(元)': 0}
credit = {'本金 (萬元) : ': 0, '期數(年) : ': 0, '年利率(%) : ': 0}
for x in credit:
    credit[x] = input(x)
t = math.ceil(float(credit['期數(年) : ']) * 12)
m = float(credit['本金 (萬元) : ']) * 10000
mt = math.ceil(m / t)
credit_for['本 金(元)'] = mt
r = float(credit['年利率(%) : ']) / 1200
for i in range(t):
    print('第' + str(i + 1) + '期')
    credit_for['利 息(元)'] = round(m * r)
    if i == t - 1:
        credit_for['本 金(元)'] = round(m)
    m -= mt
    credit_for['本金利息累計(元)'] += \
        credit_for['利 息(元)'] + credit_for['本 金(元)']
    for x in credit_for:
        print(x + ':' + format(credit_for[x], ','))