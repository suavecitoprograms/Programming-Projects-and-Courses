# Write your solution here

from string import *

def change_case(orig_string: str) -> str:
    returned = ""
    for letter in orig_string:
        if letter in ascii_lowercase:
            returned += letter.upper()
        else:
            returned += letter.lower()
    return returned

def split_in_half(orig_string: str) -> tuple:
    return (orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:])

def remove_special_characters(orig_string: str):
    returned = ""
    allowed = ascii_letters + digits + whitespace
    for letter in orig_string:
        if letter in allowed:
            returned += letter
    return returned
