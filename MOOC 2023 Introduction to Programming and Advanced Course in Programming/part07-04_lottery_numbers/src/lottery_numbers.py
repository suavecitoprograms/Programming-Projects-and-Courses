# Write your solution here
from random import *
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = list(range(lower, upper+1))
    shuffle(numbers)
    lottery_number = numbers[:amount]
    return sorted(lottery_number)
