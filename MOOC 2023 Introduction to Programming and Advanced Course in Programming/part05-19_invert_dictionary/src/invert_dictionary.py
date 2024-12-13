# Write your solution here
def invert(dictionary: dict):
    copy = {}
    
    for key in dictionary:
        copy[key] = dictionary[key]
        
    for key in copy:
        del dictionary[key]
    
    for key in copy:
        dictionary[copy[key]] = key
    
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    new = invert(s)
    print(new)\

