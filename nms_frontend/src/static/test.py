import json

data = ''

with open('items.json') as f:
    data = json.load(f)

def cascade_ingredients(item):
    '''
    - take an item
    - read its ingredients
    - check if the ingredient is baseline
    - if it is, save it
    - if it's not, call the function again and save the return value
    - return the full list of ingredients
    '''

    ingredients = {}

    if item in data.keys():
        ings = data[item]['ingredients']
        for i in ings.keys():
            if i in data.keys():
                # print("recursive trigger")
                # print("calling cascade_ingredients on '" + i + "'")
                c = cascade_ingredients(i)
                #print(c)
                for j in c:
                    # print(str(j) + ": " + str(c[j]))
                    if j in ingredients.keys():
                        ingredients[j] = ingredients[j] + c[j]
                    else:
                        ingredients[j] = c[j]
                # call the function again, but first I want to test that it breaks properly
            else:
                if i in ingredients.keys():
                    ingredients[i] = ingredients[i] + ings[i]
                else:
                    ingredients[i] = ings[i]
    else:
        print("item '" + item + "' not found, stopping")
        # I don't think this should ever happen, but it'll probably throw an error if it does
        return 0

    return ingredients
    '''
    ingredients = {}

    while True:
        if item in data.keys():
            print("item '" + item + "' in data.keys")
            l = data[item]['ingredients']
            print("ingredients: " + str(l))
            for i in l.keys():
                print("trying '" + str(i) + "'")
                if i not in data.keys():
                    print(i + " is in data.keys")
                    if i in ingredients.keys():
                        ingredients[i] = ingredients[i] + l[i]
                    else:
                        ingredients[i] = l[i]

        else:
            print("item '" + item + "' not found, stopping")
            break

    return ingredients
    '''

print("Poly Fibre: " + str(cascade_ingredients('poly_fibre')))
print("Quantum Processor: " + str(cascade_ingredients('quantum_processor')))