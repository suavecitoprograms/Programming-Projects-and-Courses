# Write your solution here
count = 0
add = 0
mean = 0
positive = 0
negative = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    add += number
    if number > 0:
        positive += 1
    else:
        negative += 1

mean = add / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {add}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")