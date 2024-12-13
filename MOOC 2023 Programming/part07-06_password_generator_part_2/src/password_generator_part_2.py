from random import *
from string import *

def generate_strong_password(length : int, my_bool1 : bool, my_bool2: bool):
    password = []
    special = "!?=+-()#"
    choice_set = ascii_lowercase
    
    if my_bool1 or my_bool2:
        if my_bool1:
            password.append(choice(digits)) ## add at least one digit if true
            choice_set += digits
        if my_bool2:
            password.append(choice(special))  ## add at least one special if true
            choice_set += special
    password.append(choice(ascii_lowercase))  ## add at least one ascii lowercase if true
    
    index = len(password)
    
    for i in range(length - index):  ## subtracting the length of the password which contains required initial values
        password.append(choice(choice_set))   
    
    printed_pw = ""
    shuffle(password)  ## shuffle to ensure initial additions of required characters are shuffled and not on the front
    for i in password:
           printed_pw += i

    return printed_pw
