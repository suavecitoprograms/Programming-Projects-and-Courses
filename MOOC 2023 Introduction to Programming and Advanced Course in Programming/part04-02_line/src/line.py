# Write your solution here
def line(x, y):
    if y == "":
        y = "*"
    print(x * y[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(4, "bobo")