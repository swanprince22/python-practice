# tuples can contain a mixed set of data types
# immutable - cannot be changed

developer = ('Alice', 34, 'Rust Developer')
print(developer[1])

name, age, job = developer
print(name)
print(age)
print(job)

# use negative indexing to access the last element in the tuple

name = 'Elizah'
print(tuple(name))

print('E' in name) #checks if an item is in a tuple

desserts = ('cake', 'pie', 'cookie', 'ice cream')
print(desserts[1:3])

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Java')
print(programming_languages.count('Rust')) # counts how many times an item appears in a tuple

print(programming_languages.index('Java')) # used to find the index where a particular item is present in a tuple

print(programming_languages.index('Java', 1, 3)) #starts the searching at index 1, ends at index 3

print(sorted(programming_languages, key=len)) 

print(sorted(programming_languages, key=True)) 




