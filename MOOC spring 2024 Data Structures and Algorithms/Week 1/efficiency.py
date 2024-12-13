import time
import random

# implementation 1
def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

# length of n/input
n = 10**7
random.seed(1)
numbers = [random.randint(1, 10**6) for x in range(n)]

print("implementation 1:")
current_time = time.time()
result = count_even_1(numbers)
end_time = time.time()
print("result:", result)
print("time: ", end_time - current_time)

print()

print("implementation 2:")
current_time = time.time()
result = count_even_2(numbers)
end_time = time.time()
print("result:", result)
print("time: ", end_time - current_time)

"""
implement 1: 0.45
implement 2: 0.30
"""