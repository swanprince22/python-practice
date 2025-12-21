# common string methods

str_1 = "hello world"
print(str_1.upper())

str_2 = "HELLO"
print(str_2.lower())

str_3 = ' hello world '
print(str_3.strip()) # removes leading and trailing characters

print(str_1.replace('hello', 'hi')) #replaces all occurences of hello

print(str_1.split()) # splits the string into a list of string

list_1 = ['hello', 'bugs']
print(' '.join(list_1)) # joins elements of an iterable into a string with a separator

print(str_1.startswith('hello')) # returns a boolean if a string starts with the specified prefix

print(str_1.endswith('hola')) # returns a boolean if a string starts with the specified suffix

print(str_1.find('world')) # returns the index of the first occurence of substring. (returns -1 if it doesnt find one)

print(str_1.count('o')) # returns the number of times a substring appears in a string

print(str_1.capitalize()) # capitalizes the first character

print(str_1.isupper()) # returns true if all letters in the string are uppercase

print(str_1.islower()) # returns true if all letters in the string are lowercase

print(str_1.title()) # returns a new string with the first letter of each word capitalized








