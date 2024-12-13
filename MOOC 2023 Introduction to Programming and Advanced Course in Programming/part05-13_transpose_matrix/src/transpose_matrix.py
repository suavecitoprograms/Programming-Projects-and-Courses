# Write your solution here
def transpose(matrix: list):
    
    for row in range(len(matrix)):
        for column in range(row, len(matrix)):
            number = matrix[row][column]
            matrix[row][column] = matrix[column][row]
            matrix[column][row] = number
            
