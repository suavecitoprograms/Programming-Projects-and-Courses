def find(t):
    n = len(t)
    best = 0
    minimum = t[0]
    minimum_index = 0
    best_index = 0
    
    total = 0
    
    for i in range(n):
        minimum = min(minimum, t[i])
        if minimum == t[i]:
            minimum_index = i
        best = max(best, t[i]-minimum)
        if best == t[i]-minimum:
            best_index = i
        
    total = best
    t[best_index] = -1
    t[minimum_index] = -1
    best = 0
    for i in range(n):
        if -1 not in t[i-1: i+1]:
            print(f"hey{t[i-1: i+1]}")
            minimum = min(minimum, t[i])
            best = max(best, t[i]-minimum)
    total += best
    return total


if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10

# approach: 
# find the max and min, 