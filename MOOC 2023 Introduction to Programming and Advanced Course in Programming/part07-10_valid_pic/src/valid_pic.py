# Write your solution here
from datetime import *

def is_it_valid(pic: str):
    ## format: ddmmyyXyyyz
    century = {"+": "18", 
               "-": "19", 
               "A": "20"}
    
    if len(pic) != 11: ## check length of PIC
        return False
    
    try:
        if datetime(int(century[pic[6]] + pic[4:6]), int(pic[2:4]), int(pic[:2])):
            pass
    except:
        return False
    
    control = f"{pic[:6]}{pic[7:10]}"
    remainder = int(control) % 31
    character = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    if pic[10] != character[remainder]:
        return False
    
    return True
