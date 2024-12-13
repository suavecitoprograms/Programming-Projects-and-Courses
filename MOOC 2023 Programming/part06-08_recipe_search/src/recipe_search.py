
def recipe_database(filename: str):
    recipe_dict = {}
    with open(filename) as new_file:
        start = True
        name = ""
        
        for line in new_file:
            if start:
                name = line.strip()
                recipe_dict[name] = []
                start = False
                
            elif line == "\n":
                start = True
                continue
           
            else:
                recipe_dict[name].append(line.strip())
                
    return recipe_dict
            
def search_by_name(filename: str, word:str):
    database = recipe_database(filename)
    found_recipes = []
    
    for recipe in database:
        if word.lower() in recipe.lower():
            found_recipes.append(recipe)
    
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    database = recipe_database(filename)
    found_recipes = []
    
    for recipe in database:
        if int(database[recipe][0]) <= prep_time:
            found_recipes.append(f"{recipe}, preparation time {database[recipe][0]} min")
    
    return found_recipes

def search_by_ingredient(filename: str, ingredient: int):
    database = recipe_database(filename)
    found_recipes = []
    
    for recipe in database:
        if ingredient in database[recipe]:
            found_recipes.append(f"{recipe}, preparation time {database[recipe][0]} min")
    
    return found_recipes
