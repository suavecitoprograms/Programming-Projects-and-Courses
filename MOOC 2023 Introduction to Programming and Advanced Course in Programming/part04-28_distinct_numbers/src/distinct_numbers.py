# Write your solution here
def distinct_numbers(a : list):
    new = []
    a.sort()
    for i in a:
        if i not in new:
            new.append(i)
    return new
    
def main(new):
    if distinct_numbers():
        print(new)
        
if __name__ == "__main__":
    main()
    