# idea is to first:
# create an ordered list from 1,..,n 
# then create a tracker which tracks the original last item's index 
# then use a for loop in the range of k which will then push back the 
# position of the original last item down 1 unit, then change the 
# tracker's value as you do so

#old version
def create(n, k):
    order = [x for x in range(1, n+1)]
    
    tracker = len(order) - 1
    last = 0
    
    for i in range(k):
        if tracker == last: ##if k > n, we choose a new tracker every n times
            last = tracker + 1 ## now i will traverse until it hits the new limit which is 1 spot ahead
            tracker = len(order) - 1
        number = order.pop(tracker)
        order.insert(tracker-1, number)
        tracker = tracker-1
        
    return order

#model version
# recursive approach
def create(n, k):
    if n == 0:
        return []
    if n - 1 <= k:
        return [n] + create(n - 1, k - (n - 1))
    else:
        return create(n - 1, k) + [n]



if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(3, 3)) # esim. [3,1,2]
    print(create(3, 4)) # esim. [3,1,2]
    print(create(10, 34))