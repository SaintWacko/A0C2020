import os
import numpy as np


def main():
    match = {}
    ingredientTotal = []
    all_ingredients = set()
    all_allergens = set()
    matched = {}
    lines = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        ingredients = line.split(' (contains ')[0]
        ingredients = ingredients.split(' ')
        ingredientTotal += ingredients
        for ingredient in ingredients:
            all_ingredients.add(ingredient)
        allergens = line.split(' (contains ')[1][:-1]
        allergens = allergens.split(', ')
        for allergen in allergens:
            all_allergens.add(allergen)
            if allergen in match:
                match[allergen].append(ingredients)
            else:
                match[allergen] = [ingredients]
    while len(match.keys()):
        for key, value in list(match.items()):
            join = set([val for val in value[0] if val not in list(matched.keys())])
            if len(value) > 1:
                for ing in value[1:]:
                    join = set(ing) & join
            if len(join) == 1:
                matched[join.pop()] = key
                del match[key]
    print(matched)
    print(all_allergens)
    # print(match)
    safe = np.setdiff1d(list(all_ingredients), list(matched.keys()), assume_unique=True)
    print(len(all_ingredients))
    print(len(safe))
    # print(safe)
    total = 0
    for ing in safe:
        total += ingredientTotal.count(ing)
    return total


if __name__ == "__main__":
    print(main())
