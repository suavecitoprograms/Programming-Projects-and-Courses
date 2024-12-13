# Write your solution here
def read_input(my_int : int, boundary1 : int, boundary2 : int):
    while True:
        try:
            number = int(input(f"Please type in a number between {boundary1} and {boundary2}"))
            if boundary1 <= number <= boundary2:
                print(f"You typed in: {number}")
                return number
            else:
                error = True
        except ValueError:
            error = True
        
        if error:
            print(f"You must type in an integer between {boundary1} and {boundary2}")

