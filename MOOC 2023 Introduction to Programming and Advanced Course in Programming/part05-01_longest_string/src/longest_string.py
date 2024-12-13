# Write your solution here
def longest(strings : list):
    longest = ""
    for word in strings:
        if len(word) > len(longest):
            longest = word
    return longest
    
def main(strings : list):
    print(longest(strings))
   
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    main(strings) 
