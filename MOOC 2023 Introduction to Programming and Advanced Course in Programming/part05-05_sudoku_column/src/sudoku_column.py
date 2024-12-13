def column_correct(sudoku: list, column_no: int):
    check = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in check:
            return False
        check.append(number)
    return True
        
    
def main(sudoku: list, column_no: int):
    column_correct(sudoku, column_no)
    print(column_correct(sudoku, column_no))

if __name__ == "__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    main(sudoku, 0)
