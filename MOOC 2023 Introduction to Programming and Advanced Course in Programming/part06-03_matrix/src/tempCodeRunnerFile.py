# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        sum_matrix = []
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")
            sum_matrix.append(row_sums(row))
        return sum(sum_matrix)
            

def matrix_max():
    with open("matrix.txt") as new_file:
        max = 0
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")
            max_matrix = row_sums(row)
        return max_matrix

    
def row_sums(row):
    start = True
    for item in row:
        item = int(item)
        if start or item > max:
            max = item
        start = False
    
    return sum(row)
    
print(matrix_max())
print(matrix_sum())
print(row_sums(matrix_max(), matrix_sum()))