'''

def block_correct(sudoku: list, row_no: int, column_no: int):
    check = []
    for row in range(row_no, row_no + 3):
        for cell in range(column_no, column_no + 3):
            number = sudoku[row][cell]
            if number > 0 and number in check:
                return False
            check.append(number)
    return True

'''