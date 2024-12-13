# write your solution here

def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}
        for line in new_file:
            row = line.split(";")
            fruits[row[0]] = float(row[1])
        return fruits
