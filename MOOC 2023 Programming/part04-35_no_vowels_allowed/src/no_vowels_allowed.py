# Write your solution here
def no_vowels(my_str : str):
    vowels = "aeiou"
    new_string = ""
    for character in my_str:
        if character not in vowels:
            new_string += character
    return new_string
    
def main(my_str : str):
    my_str = no_vowels(my_str)
    print(my_str)
    
if __name__ == "__main__":
    main("this is an example")
