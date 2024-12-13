# Write your solution here
from random import choice

def roll(die: str):
    dice = {"A": [3, 3, 3, 3, 3, 6], "B": [2, 2, 2, 5, 5, 5], "C": [1, 4, 4, 4, 4, 4]}

    return choice(dice[die])

def play(die1: str, die2: str, times: int):
    one = 0
    two = 0
    tie = 0
    
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        
        if result1 > result2:
            one += 1
        elif result2 > result1:
            two += 1
        else:
            tie += 1
            
    return one, two, tie
