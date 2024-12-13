# Write your solution here
def histogram(my_str : str):
    group = {}
    for i in range(len(my_str)):
        letter = my_str[i]
        
        if letter not in group:
            group[letter] = 0
        group[letter] += 1
    
    for key, value in group.items():
        print(f"{key}", "*" * value)

if __name__ == "__main__":
    histogram("abba")
