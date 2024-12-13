# Write your solution here
def same_chars(string, a, b):
    if a >= len(string) or b >= len(string):
        return False
    return string[a] == string[b]
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abca", 0, 3))