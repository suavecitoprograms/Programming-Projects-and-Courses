# Write your solution here

def squared(x, y):
    i = 0
    add = 0
    while i < y:
        row = x * y * y
        line = row[0 + add:y + add]
        print(line)
        i += 1
        add += y
        

# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
