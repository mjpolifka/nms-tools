import json

data = ''

with open('items.json') as f:
    data = json.load(f)

def cascade_ingredients(item):
    '''
    - take an item
    - read its ingredients
    - check if the ingredient has ingredients
    - if it doesn't, save it
    - if it does, call the function again and save the return value
    - return the full list of ingredients
    '''

    # Take an item (given to the function)

    ingredients = {}

    try:
        # read its ingredients
        ings = data[item]['ingredients']
        for i in ings.keys():
            # Check if the ingredient has ingredients
            if i not in data.keys():
                ingredients = save_ingredient(i, ings, ingredients)
            else:
                # If it does, call the function again and save the return value(s)
                c = cascade_ingredients(i)
                for j in c:
                    ingredients = save_ingredient(j, c, ingredients)
    except KeyError as e:
        print("Key error: " + e)
        return 0

    return ingredients

def save_ingredient(i, j, ingredients):
    if i in ingredients.keys():
        ingredients[i] = ingredients[i] + j[i]
    else:
        ingredients[i] = j[i]
    return ingredients

print("Poly Fibre: " + str(cascade_ingredients('poly_fibre')))
print("Quantum Processor: " + str(cascade_ingredients('quantum_processor')))