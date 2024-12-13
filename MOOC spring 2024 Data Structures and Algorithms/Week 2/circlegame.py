def create(n):
    match = [x for x in range(1, n+1)]
    correct = []
    for i in range(0, len(match[:]), 2):
        match.append(match[i])
        match.pop(i)
        correct.append(match[i+1])
        if (i+1) % 2 == 0:
            correct.append(match[i])
        else:
            number = match
            match.pop(i)
            match.append(number)

    return correct

if __name__ == "__main__":
    #print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    
    # 1 2 3 4 5 6 7
    # 1 3 5 7
    # 1 3 5 7
    # 2 4 6 1 5 3 7
    
    # 1 2 3 4 5 6 7 8 9 10 11
    # 159
    # 2 4 6 8 10 11 3 7 1, 9, 5