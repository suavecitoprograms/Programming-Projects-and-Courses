# Write your solution here

number = int(input("Please type in a number: "))

firstnum = 1

while firstnum <= number:
    secondnum = 1
    while secondnum <= number:
        print(f"{firstnum} x {secondnum} = {firstnum * secondnum}")
        secondnum += 1
    firstnum  += 1