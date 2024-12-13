
def count(s):
    #model approach
    count = 0
    total = 0
    for i in s:
        count = 0 if i == "a" else count + 1
        total += count
    return total


if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9
    # approach:
    # iterate through each position. if position is a 
    # then pass, if not iterate until it reaches a then calculate, 
    # k(k-1)//2
    """
    
    Your task is to count how many substrings 
    of a string do not contain the character a.
    
    The time complexity of the algorithm should be O(n).
    
    In a file forbidden.py, implement a function
    count that returns the desired count.
        
    
    """