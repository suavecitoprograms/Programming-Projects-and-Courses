# Write your solution here

def sum_of_positives(my_list : list):
    for i in my_list[:]:
        if i < 0:
            my_list.remove(i)
    result = sum(my_list)
    return result

def main(result):
    if sum_of_positives():
        print(f"The result is {result}")
    

if __name__ == "__main__":
    main()