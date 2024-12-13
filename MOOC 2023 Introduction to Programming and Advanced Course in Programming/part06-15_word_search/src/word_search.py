# Write your solution here

def find_words(search_term: str):
    found = []
    
    with open("words.txt") as new_file:
        for word in new_file:
            word = word.replace("\n", "")
            
            if "*" in search_term:
                if search_term[0] == "*": ## find words ending with the search term
                    if word.endswith(search_term[1:]):
                        found.append(word)
                else: ## find words starting with the search term (i.e fr* will result in from)
                    if word.startswith(search_term[:len(search_term) - 1]):
                        found.append(word)
                        
            elif "." in search_term:
                if len(word) == len(search_term):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            match = False
                    if match:
                        found.append(word)
            
            else:
                if word == search_term:
                    found.append(word)
    
    return found
