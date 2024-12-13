# Copy here code of line function from previous exercise
def line(x, y):
    if y == "":
        y = "*"
    print(x * y[0])

def triangle(size):
    # You should call function line here with proper parameters
    length = 1
    while length <= size:
        line(length, "#")
        length += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
