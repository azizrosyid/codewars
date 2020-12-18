def count_bits(n):
    result = 0
    binary = int_to_binary(n)
    for i in binary:
        if i == '1':
            result += 1
    return result


def int_to_binary(num):
    result = ''
    while num >= 1:
        result = str(num % 2) + result
        num = num // 2
    return result


count_bits(10)
