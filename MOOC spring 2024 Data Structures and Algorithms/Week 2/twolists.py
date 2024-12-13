# idea:
# do one for loop in the range of the input
# for each item in a add to the dictionary 
# with the key as the number and the index
# as the value. we could cross check by 
# checking each item in b if it's in the 
# dictionary, and if so co
def count(a, b):
    positions = {}
    
    for i in range(len(a)):
        if a[i] not in positions:
            positions[a[i]] = "a", i
        if b[i] not in positions:
            positions[b[i]] = "b", i
        else:
            if i == positions[b[i]][1]:
                del positions[b[i]]
            
    return sum([1 for value in positions.values() if value[0] == "a"])      


if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5