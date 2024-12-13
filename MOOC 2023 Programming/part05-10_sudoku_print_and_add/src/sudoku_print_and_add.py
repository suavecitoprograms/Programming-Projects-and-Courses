# Write your solution here           
def print_sudoku(sudoku):
    for row in range(len(sudoku)):
        for column in range(len(sudoku)):
            number = sudoku[row][column]
            
            if number != 0:
                print(f"{number} ", end="")
            else:
                print("_ ", end="")
                
            if (column+1) % 3 == 0:
                print(" ", end="") ## space after every 3 columns
        print()
        if (row+1) % 3 == 0:
            print() ## print new line after every 3 rows
    
            
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

def main(sudoku: list, row_no: int, column_no: int, number:int):
    print_sudoku(sudoku)
    add_number(sudoku, row_no, column_no, number)
    

if __name__ == "__main__":
    sudoku  = [
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

    print_sudoku(sudoku)