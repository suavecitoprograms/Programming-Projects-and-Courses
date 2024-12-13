# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    
    factorial = 1
    index = 1

    while index <= number:
        factorial *= index
        index += 1
    print(f"The factorial of the number {number} is {factorial}")

print("Thanks and bye!")