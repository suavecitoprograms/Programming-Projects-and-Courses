# Write your solution here
def sudoku_grid_correct(sudoku: list):
    if row_correct(sudoku):
        if column_correct(sudoku):
            if block_correct(sudoku):
                return True
    return False
    
def row_correct(sudoku: list):
    check = []
    for row in sudoku:
        for cell in row:
            if cell > 0 and cell in check:
                return False
            check.append(cell)
        check = []
        
    return True

def column_correct(sudoku: list):
    check = []
    for column in range(len(sudoku)):
        for row in sudoku:
            number = row[column]
            if number > 0 and number in check:
                return False
            check.append(number)
        check = []
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
    

if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
    [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
    [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
    ]
    print(sudoku_grid_correct(sudoku))
