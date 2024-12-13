def sudoku_grid_correct(sudoku: list):
    if row_correct(sudoku):
        if column_correct(sudoku):
            if block_correct(sudoku):
                return True
    return False
    
def row_correct(sudoku: list):
    for row in sudoku:
        for cell in row:
            if row.count(cell) > 1 and cell != 0:
                return False
    return True

def column_correct(sudoku: list):
    check = []
    for column in range(len(sudoku)):
        for row in sudoku:
            number = row[column]
            if number > 0 and number in check:
                return False
            check.append(number)
    return True

def block_correct(sudoku: list):
    boundaries = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    
    check = []
    
    for boundary in boundaries:
        row_no = boundary[0]
        column_no = boundary[1]
        
        for row in range(row_no, row_no + 3):
            for cell in range(column_no, column_no + 3):
                number = sudoku[row][cell]
                if number > 0 and number in check:
                    return False
                check.append(number)
        check = []
    return True

def main(sudoku : list):
    print(sudoku_grid_correct(sudoku))