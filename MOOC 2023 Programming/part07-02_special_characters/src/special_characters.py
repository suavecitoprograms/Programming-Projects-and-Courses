# Write your solution here
from string import *
def separate_characters(my_string: str):
    first_part = ""
    second_part = ""
    third_part = ""
    
    for letter in my_string:
        if letter in ascii_letters:
            first_part += letter
        elif letter in punctuation:
            second_part += letter
        else:
            third_part += letter

    return first_part, second_part, third_part