# idea is to create a recursive approach
# iterating through each value and if it 
# is of type list then call the recursive 
# function which will iterate through its 
# respective values

def count(t):
    result = 0
    for number in t:
        if type(number) is list:
            result += count(number)
        else:
            result += 1
    return result
        
            
    

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8
