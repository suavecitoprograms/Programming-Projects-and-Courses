# Write your solution here
def shortest(my_list : list):
    shortest = my_list[0]
    for item in my_list:
        if len(item) < len(shortest):
            shortest = item
    return shortest

def main(longest):
    if shortest():
        print(shortest)
        
if __name__ == "__main__":
    main()
    