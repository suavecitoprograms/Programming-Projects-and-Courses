def find(t):
    hash = {}
    for i in t:
        if i not in hash:
            hash[i] = 0
        hash[i] += 1
        if hash[i] > 1 and len(hash) == 2:
            break
    
    for i, j in hash.items():
        if j == 1:
            return i
# idea: 
# iterate through each position and have an empty string: ""
# for first occurrence of a number add that to the front 
# and for the second add that to the back.  
# then divide and round down the len of that string to get the middle position 
# that will be the number with the most occurrence
# 1 1 1 1 2 2 2

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5