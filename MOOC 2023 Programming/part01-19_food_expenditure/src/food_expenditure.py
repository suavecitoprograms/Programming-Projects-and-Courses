# Write your solution here

student_caf_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_studentlunch = float(input("The price of a typical student lunch? "))
groceries_week = float(input("How much money do you spend on groceries in a week? "))

weekly = (student_caf_week * price_studentlunch) + groceries_week
daily = weekly/7


print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")

