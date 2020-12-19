def valid_solution(board):
    for i in board:
        if i.count(0) >= 1:
            return False

    temp = []
    for i in range(len(board)):
        for j in range(len(board)):
            temp.append(board[j][i])
        if len(temp) != len(set(temp)):
            return False
        temp = []

    for i in range(len(board)):
        for j in range(len(board)):
            temp.append(board[i][j])
        if len(temp) != len(set(temp)):
            return False
        temp = []

    for i in range(0, 8, 3):
        for k in range(0, 8, 3):
            for j in range(i, i+3):
                temp.extend(board[j][k:k+3])
            if len(temp) != len(set(temp)):
                return False
            temp = []

    return True


print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                      [4, 9, 8, 2, 6, 1, 3, 7, 5],
                      [7, 5, 6, 3, 8, 4, 2, 1, 9],
                      [6, 4, 3, 1, 5, 8, 7, 9, 2],
                      [5, 2, 1, 7, 9, 3, 8, 4, 6],
                      [9, 8, 7, 4, 2, 6, 5, 3, 1],
                      [2, 1, 4, 9, 3, 5, 6, 8, 7],
                      [3, 6, 5, 8, 1, 7, 9, 2, 4],
                      [8, 7, 9, 6, 4, 2, 1, 3, 5]]
                     ))
