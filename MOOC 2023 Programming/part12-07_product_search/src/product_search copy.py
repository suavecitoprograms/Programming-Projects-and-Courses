# Write your solution here


def search(products: list, criterion: callable = lambda x: True):
    return [product for product in products if criterion(product)]
