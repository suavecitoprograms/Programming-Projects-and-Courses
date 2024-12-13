# Write your solution here

limit = int(input("Limit: "))
number = 1
sum = 1
addition = "1"
while sum < limit:
    number += 1
    addition += f" + {number}"
    sum += number
print(f"The consecutive sum: {addition} = {sum}")