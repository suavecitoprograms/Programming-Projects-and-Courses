x = [1,2,1,3,5,1,4,3,1,3]

def max_length(numbers:list):
    pos = {}
    start = 0
    length = 0
    n = len(numbers)
    
    for i, song in enumerate(numbers):
        if song in pos:
            start = pos[song] + 1
        pos[song] = i
        length = max(length, i - start + 1)
        
    return length

print(max_length(x))