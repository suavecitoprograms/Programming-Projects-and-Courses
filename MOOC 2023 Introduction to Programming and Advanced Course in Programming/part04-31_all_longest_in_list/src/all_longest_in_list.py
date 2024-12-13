# Write your solution here
def all_the_longest(my_list : str):
    list = []
    
    for item in my_list:
        if list == [] or len(item) > len(list[0]):
            list = [item]
        elif len(item) == len(list[0]):
            list.append(item)
            
    return list

def main():
    print(list)
    
if __name__ == "__main__":
    main()
    

