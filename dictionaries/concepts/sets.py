# sets - doesn't store duplicate values
# mutable and unordered

my_set = {1 ,2 ,3 ,4 ,5}

set() #set
{} #dictionary

my_set.add(6)

my_set.remove(5)

print(my_set)

# .remove() will throw an error if the element is not found
# .discard() will not

#my_set.clear() # removes all elemebts from the set

first_set = {1, 2 ,3 ,4, 5}
second_set = {2, 3, 4, 6}

print(second_set.issubset(first_set)) # checks if all elements of 2nd set is in first set
print(first_set.issuperset(second_set)) # checks if first set have all of the elements in second set

print(first_set.isdisjoint(second_set)) # checks if two sets are disjoint, have no common elements

first_set | second_set # returns a new set will all the elements from both sets

first_set & second_set # returns a new set with only the elements that the sets have in common

first_set - second_set # returns a new set with the elements in either the first or second set but not both

first_set ^ second_set # returns a new set with elements either in the first or second set but not both

# |= &= -= ^=
# automatically asigns the resulting set to the first set in the expression

first_set -= second_set # finds the difference between the sets and updates the first set with that result

print(first_set)

print(5 in first_set) # use in operator to check if an element is in a set



