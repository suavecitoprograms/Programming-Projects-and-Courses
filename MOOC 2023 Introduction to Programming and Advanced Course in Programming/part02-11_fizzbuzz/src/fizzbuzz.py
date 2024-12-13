# Write your solution here
number = int(input("Number: "))

name = ""

if number % 3 == 0:
    name += "Fizz"

if number % 5 == 0:
        name += "Buzz"

print(f"{name}")