puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def sudoku(puzzle):
    coordinate_unsolved = []
    for row_index, row in enumerate(puzzle):
        for number_index, number in enumerate(row):
            if number == 0:
                coordinate = [row_index,number_index]
                coordinate_unsolved.append(coordinate)
    pretty_print(puzzle)

    i = 0
    action = 0
    while i != len(coordinate_unsolved):
        action += 1
        row_index, number_index = coordinate_unsolved[i]
        block = [number_index//3, row_index//3]
        puzzle[row_index][number_index] += 1
        if puzzle[row_index][number_index] == 10:
            puzzle[row_index][number_index] = 0
            i -= 1
        elif validate_block(puzzle, block) and validate_row(puzzle[row_index]) and validate_vertical(puzzle, number_index):
            i += 1
    print(action)
    pretty_print(puzzle)
    return puzzle

def pretty_print(puzzle):
    for row in puzzle:
        print(row)
    print()

def validate_block(puzzle, coordinate_block):
    number_index, row_index = coordinate_block
    number_index, row_index = number_index*3, row_index*3
    number_block = []
    for i in range(3):
        for j in range(3):
            number_block.append(puzzle[row_index+i][number_index+j])
    return validate_number(number_block)


def validate_row(row):
    return validate_number(row)


def validate_vertical(puzzle, x):
    list_number = []
    for i in range(len(puzzle)):
        list_number.append(puzzle[i][x])
    return validate_number(list_number)


def validate_number(list_number):
    number_store = []
    for number in list_number:
        if number != 0:
            if not (number in number_store):
                number_store.append(number)
            elif number in number_store:
                return False
    return True


                


print(sudoku(puzzle))

