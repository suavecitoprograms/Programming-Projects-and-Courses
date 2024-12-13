# Write your solution here
def factorials(n: int):
    factorial_pairs = {}
    factorial_pairs[1] = 1
    
    for numbers in range(2, n+1):
        factorial_pairs[numbers] = factorial_pairs[numbers-1] * numbers
        
    return factorial_pairs

    
    
if __name__ == "__main__":
    k = factorials(3)
    print(k)
    
####
#     factorial_pairs = {}
#    factorial = 1
    
#   for numbers in range(1, n+1):
#      for item in range(1, numbers+1):
   #         factorial *= item
    #    factorial_pairs[numbers] = factorial
    #    factorial = 1
   # return factorial_pairs
# ####