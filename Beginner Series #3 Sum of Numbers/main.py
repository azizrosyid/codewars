def get_sum(a, b):
    result = 0
    gap = 0
    if a > b:
        b -= 1
        gap = -1
    elif a < b:
        b += 1
        gap = 1
    elif a == b:
        return a

    for i in range(a, b, gap):
        result += i
    return result


print(get_sum(5, 11))
