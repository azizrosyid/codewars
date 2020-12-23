def to_roman(number):
    lengthDigit = len(str(number))
    romanM, number = divmod(number, 1000)
    romanC, number = divmod(number, 100)
    romanX, number = divmod(number, 10)
    romanI = number

    strRoman = "M" * romanM + "C"*romanC+"X"*romanX + "I" * romanI
    # if strRoman.count("C") >= 5:

    # print(strRoman)


to_roman(1990)
