# Copy here code of line function from previous exercise and use it in your solution
def line(x, y):
    if y == "":
        y = "*"
    print(x * y[0])

def triangle(size, character1):
    length = 1
    while length <= size:
        line(length, character1)
        length += 1

def rectangle(size, character2, height):
    while height > 0:
        line(size, character2)
        height -= 1

def shape (a, b, c, d):
    triangle(a, b)
    rectangle(a, d, c)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")
    
