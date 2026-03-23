for num in range(3):
    print(num)

print('----')

for num in range(1, 5):
    print(num)

print('----')


for num in range(2, 11, 2):
    print(num)

print('----')


for num in range(40, 0, -10): #decrements
    print(num) 

print('----')

numbers = list(range(2, 11, 2)) #converts an iterable into a list
print(numbers)

print('----')

languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages))) #  each tuple now contains a count

for index, langauge in enumerate(languages, 1):
    print(f'Index {index} and langugage {langauge}')

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

