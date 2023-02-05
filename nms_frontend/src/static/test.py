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

    if item in data.keys(): # This should be a try/catch block for readability
        # read its ingredients
        ings = data[item]['ingredients']
        for i in ings.keys():
            # Check if the ingredient has ingredients
            if i not in data.keys():
                ingredients = save_ingredient(i, ings, ingredients)
                '''
                # If it doesn't, save it
                if i in ingredients.keys():
                    # If this ingredient is already on the list, add to it
                    ingredients[i] = ingredients[i] + ings[i]
                else:
                    # Otherwise add it to the list (is there a python function that can simplify this?)
                    ingredients[i] = ings[i]
                '''
            else:
                # If it does, call the function again and save the return value
                c = cascade_ingredients(i)
                for j in c:
                    ingredients = save_ingredient(j, c, ingredients)
                    '''
                    if j in ingredients.keys():
                        ingredients[j] = ingredients[j] + c[j]
                    else:
                        ingredients[j] = c[j]
                    '''
    else:
        # This should probably be a try/catch
        print("item '" + item + "' not found, stopping")
        # I don't think this should ever happen, but it'll probably throw an error if it does
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