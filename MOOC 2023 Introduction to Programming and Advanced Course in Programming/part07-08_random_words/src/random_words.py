# Write your solution here
from random import sample

def words(n: int, beginning: str):
    words = []
    with open("words.txt") as new_file:
        for line in new_file:
            if line.startswith(beginning):
                words.append(line.strip())
    if n > len(words):
        raise ValueError("There are not enough words beginning with the specified string")
    
    return sample(words, n)
