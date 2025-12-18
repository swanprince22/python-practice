# introduction to python -- freecodecamp

print("Hello, World!")
name = 'Elizah'
age = 25

# variable names should be in lowercase

print(name, age)

set = {1, 2, 3} # unordered collection of unique elements
print('Set:', set)
# use parenthesis () to make it immutable

dictionary = {'name:' 'Alice', 'age:', 25}  # collection of key-value pairs
print(dictionary)

range_var = range(5) # sequence of numbers, often used in loops

list_var = [22, 'Hello world', 3.14, True] # ordered collection of elemens that support different data types

none_var = None # special value that represents the absence of a value
print('None:', none_var)

# all data are treated as objects
# immutable data: string, int, float, boolean, tuple, range

print(type(age))

print(isinstance(25, int))
print(isinstance(25, str))

def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}'

user_name: str = 'bub'
user_age: int = 1

print(greet(user_name, user_age))

