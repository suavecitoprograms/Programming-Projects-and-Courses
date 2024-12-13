hourlywage = float(input("Hourly wage: "))
hoursworked = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday == "Sunday":
    hourlywage *= 2

totalwage = hourlywage * hoursworked
print(f"Daily wages: {totalwage} euros")