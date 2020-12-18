def snail(snail_map):
    result = []
    n = len(snail_map)
    n2 = 0
    if snail_map[0] == []:
        return []
    while not (n == 0):
        for i in range(n):
            elem = snail_map[n2][i]
            if elem not in result:
                result.append(elem)
        for i in range(n):
            elem = snail_map[i][n-1]
            if elem not in result:
                result.append(elem)
        for i in range(n-1, -1, -1):
            elem = snail_map[n-1][i]
            if elem not in result:
                result.append(elem)
        for i in range(n-1, -1, -1):
            elem = snail_map[i][n2]
            if elem not in result:
                result.append(elem)
        if n == n2 or n2 > n:
            break
        n -= 1
        n2 += 1
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

snail(array)
