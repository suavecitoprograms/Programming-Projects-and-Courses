# write your solution here
def read():
    m = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            mrow = []
            items = line.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
            
        return m

def combine(m):
    cumulative = []
    for row in m:
        cumulative += row
    return cumulative

def matrix_sum():
    m = combine(read())
    return sum(m)
            
def matrix_max():
    m = combine(read())
    return max(m)
    
def row_sums():
    collection = read()
    sumss = []
    for row in collection:
        sumss.append(sum(row))
    return sumss
        

