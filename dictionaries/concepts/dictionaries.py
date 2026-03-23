pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
# passes a list

print(pizza['name'])

pizza['name'] = 'Margherita'

print(pizza['name'])

pizza.get('toppings', [])
# returns an empty set if the key doesnt exist

print(pizza.keys()) #returns view object of the keys

print(pizza.values()) #returns view object of the values

print(pizza.items()) #returns view object of the key-value pairs

#pizza.clear() removes all the key-value pairs from the dictionary

pizza.pop('price', 10)

pizza.popitem() # removes the last inserted item

pizza.update({ 'price': 15, 'total_time': 25 })

