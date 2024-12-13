# Write your solution here
def chessboard(x):
    i = 0
    while i < x:
        if i % 2 == 0:
            row = "10" * x
        else:
            row = "01" * x
        i += 1
        print(row[0:x])
        

# Testing the function
if __name__ == "__main__":
    chessboard(7)
