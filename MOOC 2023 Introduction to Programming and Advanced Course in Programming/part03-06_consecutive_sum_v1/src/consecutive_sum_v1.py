# Write your solution here

limit = int(input("Limit: "))
number = 0
sum = 0

while sum < limit:
    number += 1
    sum += number
print(sum)
