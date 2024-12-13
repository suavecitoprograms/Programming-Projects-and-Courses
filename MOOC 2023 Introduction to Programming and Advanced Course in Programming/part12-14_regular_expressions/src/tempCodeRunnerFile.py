def time_of_day(my_string: str): # XX:YY:ZZ
    if re.search("^[0-1][0-9]|[2][0-4]:[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    return False
if __name__ == "__main__":
    print(time_of_day("23:zz:59"))