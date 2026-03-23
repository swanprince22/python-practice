programming_langauges = ['Rust', 'Java', 'Python', 'C++', 'Rust']

for language in programming_langauges:
    print(language)

for char in 'code':
    print(char)

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana'] 

for category in categories:
    for food in foods:
        print(category, food)

secret_number = 3
guess = 0

# while guess != secret_number:
#     guess = int(input('Guees the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')

# print('You got it!')

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer) #prints Jess

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer) #prints Jess, Tom

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' containd the vowel'{letter}'")
            break
    
    else:
        print(f"'{word}' has no vowels")

