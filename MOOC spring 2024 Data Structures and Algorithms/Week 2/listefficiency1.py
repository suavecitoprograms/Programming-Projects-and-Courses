import time
import random

info = []
def list_efficiency_addition(n:int):
    for i in range(n):
        info.append(i)
def list_efficiency_deletion(n:int):
    for i in range(n-1, 0, -1):
        info.pop(-1)

## time complexity testing
n = 10**5
random.seed(1812)
number = random.randrange(1, n)

print("addition: ")
start_time_add = time.time()
list_efficiency_addition(number)
end_time_add = time.time()
print(number)
print("time:", round(end_time_add-start_time_add,5))

print("deletion: ")
start_time_del = time.time()
list_efficiency_deletion(number)
end_time_del = time.time()
print(number)
print("time:", round(end_time_del-start_time_del,5))