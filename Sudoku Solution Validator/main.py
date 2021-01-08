# def valid_solution(board):
#     for i in board:
#         if i.count(0) >= 1:
#             return False

#     temp = []
#     for i in range(len(board)):
#         for j in range(len(board)):
#             temp.append(board[j][i])
#         if len(temp) != len(set(temp)):
#             return False
#         temp = []

#     for i in range(len(board)):
#         for j in range(len(board)):
#             temp.append(board[i][j])
#         if len(temp) != len(set(temp)):
#             return False
#         temp = []

#     for i in range(0, 8, 3):
#         for k in range(0, 8, 3):
#             for j in range(i, i+3):
#                 temp.extend(board[j][k:k+3])
#             if len(temp) != len(set(temp)):
#                 return False
#             temp = []

#     return True

def valid_solution(board):
    block = validate_block(board)
    row_horizontal = validate_row(board)
    row_vertical = validate_row(transpose(board))
    return block and row_horizontal and row_vertical
    

def validate_block(board):
    for x in range(0,9,3):
        for y in range(0,9,3):
            number_block = get_block(board,x,y)
            if not validate_number(number_block):
                return False
    return True

def validate_row(board):
    for list_number in board:
        if not validate_number(list_number):
            return False
    return True

def transpose(board):
    result = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            row.append(board[j][i])
        result.append(row)
    return result

def get_block(board,x,y):
    number_block = []
    for i in range(3):
        for j in range(3):
            number_block.append(board[x+i][y+j])
    return number_block

def validate_number(list_number):
    valid_number = [1,2,3,4,5,6,7,8,9]
    return sorted(list_number) == valid_number



print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
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
