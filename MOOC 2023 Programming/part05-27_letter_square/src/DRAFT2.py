def alphabet():
    alphabet_list = [
        "A","B","C","D","E","F","G","H","I",
        "J","K","L","M","N","O","P","Q","R",
        "S","T","U","V","W","X","Y","Z"]
    assignment = {}
    
    for i in range(0, 26):
        assignment[i+1] = alphabet_list[i]
    
    return assignment

def matrix(layer : int, assignment : dict):
    dimension = layer * 2 - 1
    matrix = []

    for row in range(0, dimension):
        matrix.append([])
    
    for row in range(0, dimension):
        for column in range(0, dimension):
            matrix[row].append("")
        
    return matrix, dimension

def printers(layer, assignment, matrix, dimension):
    start_index = 0
    end_index = dimension
        
    for letter in range(layer, 0, - 1): ## traversing through letters
        length = letter * 2 - 1
        for cell in range(start_index, end_index):     ## traversing through rows
            matrix[start_index][cell] = assignment[letter]
            matrix[end_index - 1][cell] = assignment[letter]
        
        for column in range(dimension):
            for row in range(start_index + 1, end_index - 1):
                matrix[row][start_index] = assignment[letter]
                matrix[row][end_index-1] = assignment[letter]                
        
        start_index += 1
        end_index -= 1
        

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


def main(layer):
    assignment = alphabet()
    matrices, dimension = matrix(layer, assignment)
    
    printers(layer, assignment, matrices, dimension)
    
    ## print out for visuals
    for row in matrices:
        for column in row:
            print(column, end="")
        print()
    
    
main(4)