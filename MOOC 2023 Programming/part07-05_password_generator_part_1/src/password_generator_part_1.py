# Write your solution here
# Write your solution here
from random import *
from string import *

def generate_password(length : int):
    password = ""
    for i in range(length):
        password += choice(ascii_lowercase)
    return password
