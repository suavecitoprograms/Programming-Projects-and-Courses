# model solution approach 
# find minimum with min 
# find first and last occurrence of minimum 
# return the difference of the index of the latter to the former 
def count(t):
    minimum = min(t)
    first = t.index(minimum)
    last = len(t) - t[::-1].index(minimum) - 1
    return last - first

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0
    
# problem at hand is asking how many ways can we divide the list into two segments 
# while retaining the same smallest number 
# 
# approach: 
# find the minimum by using min method i.e ( min(t) ) 
# iterate through each index if number at that index is not the minimum, we just continue 
# if the number is the first occurrence of the minimum, we set the total to 0, 
# now after every iteration where the number at the index is not the minimum we increment total 
# if we encounter the second occurrence we return total, breaking the loop