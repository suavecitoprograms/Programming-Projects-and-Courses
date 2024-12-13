# Write your solution here
def spruce(a):
    print("a spruce!")
    a = a * 2 - 1
    index = 1
    while index <= a:
        whitespace = (a - index) // 2
        print(whitespace * " " + index * "*" + whitespace * " " )
        index += 2
    print(((a - 1) // 2) * " " + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)
    
