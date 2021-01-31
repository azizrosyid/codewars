# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd[0] if len(odd) < len(even) else even[0]

find_outlier([160, 3, 1719, 19, 11, 13, -21])