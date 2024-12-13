# Write your solution here
def negative_positive():
    number = int(input("Please type in a number: "))
    for i in range(-number, number + 1):
        if i != 0:
            print(i)

negative_positive()