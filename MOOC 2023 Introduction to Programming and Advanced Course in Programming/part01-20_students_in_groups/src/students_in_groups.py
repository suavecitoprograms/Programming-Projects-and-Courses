# Write your solution here

students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

group = (students + size - 1) // size

print(f"Number of groups formed: {group}")