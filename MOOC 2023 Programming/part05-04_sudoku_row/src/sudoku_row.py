# Write your solution here
def row_correct(sudoku: list, row_no: int):
    for cell in sudoku[row_no]:
        if sudoku[row_no].count(cell) > 1 and cell != 0:
            return False
    return True

    
def main(sudoku: list, row_no: int):
    row_correct(sudoku, row_no)

