# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        start = True
        for number in new_file:
            if start or int(number) > largest:
                largest = int(number)
            start = False
    return largest
