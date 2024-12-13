# Write your solution here
from datetime import * 
def age_millennium():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    
    ## millennium is the year 200
    
    birth = datetime(year, month, day)
    millennium = datetime(1999, 12, 31)
    
    if birth >= millennium:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        age_milly = millennium - birth
        print(f"You were {age_milly.days} days old on the eve of the new millennium.")

age_millennium()