# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    month = 0
    savingMoney = 0
    while savingMoney + startPriceOld < startPriceNew:
        month += 1
        if month % 2 == 0:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld * percentLossByMonth / 100
        startPriceNew -= startPriceNew * percentLossByMonth / 100
        savingMoney += savingperMonth
    return [month, round(startPriceOld+savingMoney - startPriceNew)]


print(nbMonths(2000, 8000, 1000, 1.5) == [6, 766])
print(nbMonths(12000, 8000, 1000, 1.5) == [0, 4000])
