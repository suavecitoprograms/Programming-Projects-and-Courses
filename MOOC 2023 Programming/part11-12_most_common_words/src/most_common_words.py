# WRITE YOUR SOLUTION HERE:
from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as new_file:
        info = new_file.read()
        for punctuation_marks in punctuation:
            info = info.replace(punctuation_marks, "")
        info = info.strip().split()        
    # trying to remove line breaks and punctuation
    return {word: info.count(word) for word in info if info.count(word) >= lower_limit}
