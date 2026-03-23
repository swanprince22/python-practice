products = {
    'Laptop': 900,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

print('-----------------')

for product in products.keys():
    print(product)

print('-----------------')

for product in products.items():
    print(product)

print('-----------------')

for product, price in products.items():
    print(product, price)

print('-----------------')

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

print('-----------------')

for product in enumerate(products):
    print(product)

print('-----------------')

for index, product in enumerate(products):
    print(index, product)

print('-----------------')

for price in enumerate(products.values()): # if need to iterate over the values
    print(price)

print('-----------------')

for index, product in enumerate(products.items()):
    print(index, product)

print('-----------------')

for index, product in enumerate(products.items(), 1): # customizes the initial value of count
    print(index, product)