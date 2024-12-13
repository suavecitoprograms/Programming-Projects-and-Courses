    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("alcohol free beer", 24)
    my_list.add("pineapple", 1)

    print("the shopping list contains at least 8 of the following items:")
    for product in products_in_shopping_list(my_list, 8):
        print(product)