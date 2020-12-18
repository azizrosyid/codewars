def decimalToHex(number):
    hex = ""
    alphabet = "ABCDEFG"
    while True:
        hexAppend = number % 16
        if hexAppend > 9:
            hexAppend = alphabet[hexAppend-10]
        hex += str(hexAppend)
        number = number // 16
        if number == 0:
            break
    hex = hex[::-1]
    return hex


def rgb(r, g, b):
    rgb = [r, g, b]
    for i in range(len(rgb)):
        if rgb[i] > 255:
            rgb[i] = 255
        elif rgb[i] < 0:
            rgb[i] = 0
    for i in range(len(rgb)):
        rgb[i] = decimalToHex(rgb[i])
        if len(rgb[i]) == 1:
            rgb[i] = "0" + rgb[i]
    return "".join(rgb)


print(rgb(255, 255, 255))
