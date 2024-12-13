# Write your solution here

def find_words(search_term: str):
    search_term = search_term.lower()
    ## first part is to make a dictionary that has all words in words.txt
    word_list = []
    with open("words.txt") as new_file:
        for word in new_file:
            word_list.append(word.strip())
     
    found = []
    ## first wild card
    if "." in search_term:
        index = []
        for i in range(len(search_term)):
            if search_term[i] == ".":
                index.append(i)

        match = True
        for word in word_list:
            if len(word) == len(search_term):
                match = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                if match:
                    found.append(word)                
    
    ## second wild card
    elif "*" in search_term:
        if search_term[0] == "*":
            for word in word_list:
                if word[(len(word) - len(search_term[1:])):] == search_term[1:]: ## if the last portions of a word == the searchterm then return
                    found.append(word)
        
        elif search_term[len(search_term)-1] == "*":
            for word in word_list:
                if word[:len(search_term[:-1]):] == search_term[:-1]: ## if the first portions of a word == the searchterm then return
                    found.append(word)
                    
        return found

                    
    else:
        if search_term in word_list:
            found.append(search_term)
    
    return found
