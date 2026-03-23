numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

even_numbers = [8, 10, 12]
#numbers.append(even_numbers)
print(numbers)

numbers.extend(even_numbers) # adds the elements from the list individually
print(numbers)

numbers.insert(6, 7) # insert element at a specific index
print(numbers)

numbers.remove(12) # removes an element
numbers.pop(1) #remove element at a specific index

print(numbers.clear()) # removes all elements from the list

print(numbers.sort()) #sorts in ascending

sorted(numbers) # returns a new sorted list instead of modifying the original list

numbers.reverse() # reverses a list of elements

prog_lang = ['Rust', 'Java', 'Python']
print(prog_lang.index('Rust')) # finds the index of the element

