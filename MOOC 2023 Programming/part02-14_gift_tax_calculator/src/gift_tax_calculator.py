# Write your solution here

value = int(input("Value of gift: "))
lowertax = 0
taxrate = 0
deduct = 0

if value < 5000:
    taxamount = "No tax"

if 5000 <= value <= 25000:
    lowertax = 100
    taxrate = .08
    deduct = 5000

if 25000 <= value <= 55000:
    lowertax = 1700
    taxrate = .1
    deduct = 25000

if 55000 <= value <= 200000:
    lowertax = 4700
    taxrate = .12
    deduct = 55000

if 200000 <= value < 1000000:
    lowertax = 22100
    taxrate = .15
    deduct = 200000

if value >= 1000000:
    lowertax = 142100
    taxrate = .17
    deduct = 1000000

if value >= 5000:
    taxamount = lowertax +  (value - deduct) * taxrate
    print(f"Amount of tax: {taxamount} euros")

else:
    print("No tax")
