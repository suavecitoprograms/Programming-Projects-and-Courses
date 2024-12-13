# Copy here code of line function from previous exercise
def line(x, y):
    if y == "":
        y = "*"
    print(x * y[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    length = size
    while size > 0:
        line(length, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
