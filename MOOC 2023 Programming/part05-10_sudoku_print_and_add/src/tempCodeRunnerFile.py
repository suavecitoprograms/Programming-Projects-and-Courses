def print_sudoku(sudoku):
    for row in sudoku:
        if sudoku[row] % 3 == 0:
            print()
        for column in row:
            if column % 3 == 0:
                print(" ", end="")
            number = sudoku[row][column]
            if number == 0:
                print("_ ", end="")
            else:
                print(f"{number} ", end="")