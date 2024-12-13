"""
def count(s):
    #iterative approach
    one_count = 0
    zero_count = 0
    total = 0
    for i in s:
        if i == "1":
            total += one_count
            one_count += 1
        else:
            total += zero_count
            zero_count += 1
    return total
"""

def count(s):
    # one-liner approach
    one_count = s.count("1")
    zero_count = s.count("0")

    return one_count*(one_count-1)//2 + zero_count*(zero_count-1)//2

if __name__ == "__main__":
    print(count("0101")) # 2
    # 1: index 1, index 3
    # 2: index 0, index 2
    print(count("000000")) # 15
    6 * (6-1)//2 
    6*(6-1)//2
    0
    
    print(count("000111")) # 6
    print(count("00100001101100")) # 46
    # approach:
    # iterate through each position, for every occurrence of 
    # 1 or 0, add count to total then
    # increment 1 to each count.
    
    """
    
    You are given a bit string that consists of the characters 0 and 1. 
    How many ways can you choose two positions in the bit string so that 
    each position has the same bit?
    The time complexity of the algorithm should be O(n).
    In a file samebit.py, implement a function count that returns the desired count.
        
        
    """