# Write your solution here
import re

def is_dotw(my_string: str):
    if re.search("^MON|TUE|WED|THU|FRI|SAT|SUN$",my_string.upper()):
        return True
    return False

def all_vowels(my_string: str):
    if re.search("^[aeiou]+$", my_string.lower()):
        return True
    return False
def time_of_day(my_string: str): # XX:YY:ZZ
    if re.search("^([0-1][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    return False

if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))