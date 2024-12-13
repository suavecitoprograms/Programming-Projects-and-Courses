# write your solution here
def matrix_sum():
    with open("matrix.txt") as new_file:
        sum_matrix = []
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")

            sum_matrix.append(sum_max(row)[1])
        return sum(sum_matrix)
            

def matrix_max():
    with open("matrix.txt") as new_file:
        start = True
        largest = None
        
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")
            row_largest = sum_max(row)[0]
            
            if start or row_largest > largest:
                largest = row_largest
            start = False
                
        return largest
    
def row_sums():
    with open("matrix.txt") as new_file:
        sum_of_rows = []
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(",")
            sum_of_rows.append(sum_max(row)[1])
        
        return sum_of_rows
    
def sum_max(row):
    start = True
    largest = None
    for i in range(len(row)):
        row[i] = int(row[i])
        if start or row[i] > largest:
            largest = row[i]
        start = False
    
    return largest, sum(row)
