def count(s):
    #model solution approach
    n = len(s)
    count = 0
    total = 0
    for i in range(n):
        if s[i] != s[i-1]:
            count = 0
        count += 1
        total += count
    return  total

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
    # approach: 
    # iterate through each index 
    # if letter in index is different from the previous one 
    # reset the count to 1, if not add 1 
    # then increment the total by count    
    """
    
    A substring is a contiguous string inside a string. 
    For example, the substrings of the string abc are 
    a, b, c, ab, bc and abc. 
    Your task is to count how 
    many substrings have the same character at all positions.
    
    
    The time complexity of the algorithm should be O(n).
    In a file samechar.py, implement a function count that 
    returns the desired count.
        
    """