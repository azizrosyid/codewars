def zeros(n):
    zero = 0
    while n >= 5:
        zero += n // 5
        n = n//5

    return zero


print(zeros(100))
