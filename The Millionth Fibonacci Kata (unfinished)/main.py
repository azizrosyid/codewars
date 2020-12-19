# def fib(n):
#     n1 = 0
#     n2 = 1
#     if n == 0:
#         return 0
#     if n == 1:
#         return n2
#     counter = 0
#     result = 0
#     while n-1 > counter:
#         result = n1 + n2
#         n1 = n2
#         n2 = result
#         counter += 1
#     return result

def fib(n):
    if n in [0, 1]:
        return n
    else:
        return (fib(n-1))+(fib(n-2))


print(fib(5))
