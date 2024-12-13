# Write your solution here
def hash_square(x):
    length = x
    while x > 0:
        print(length * "#")
        x -= 1
        



# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)