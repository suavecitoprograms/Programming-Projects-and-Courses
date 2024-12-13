# Write your solution here
def find_word(sentence, number):
    counter = 0
    word = ""
    wordcount = 0
        
    while counter < len(sentence):
        if sentence[counter] == " ":
            wordcount += 1
            if wordcount == number:
                break
            word = ""
        else:
            word += sentence[counter]
        counter += 1
    return word

def first_word(sentence):
    return find_word(sentence, 1)
 
def second_word(sentence):
    return find_word(sentence, 2)
 
def last_word(sentence):
    return find_word(sentence, 0) 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))