# strings

msg = 'It\'s a sunny day' # use \ to escape the single or double quotation marks
print(msg)

str_1 = 'Hello'
str_2 = 'World'
sentence = str_1 + ' ' + str_2 # works only with string. (string + int = error)
print(sentence)

name = "John Doe"
age = 5
print(name + str(age))

name = "Monroe"
name_and_age = name
name_and_age += str(age)
print(name_and_age)

sentence = f"My name is {name} and I am {age} years old."
print(sentence)

print(len(name)) # monroe

print(name[0])
print(name[5])

print(name[-1]) #starts with the last character

#string slicing

print(name[0:3]) # 3 is non-inclusive
print(str_2[1:])
print(str_2[:]) # extracts the whole string

# step parameter - string[start:stop:step]
str_3 = "Hello world"
print(str_3[0:11:2])

print(str_3[::-1]) # reverses the string

print('f' in str_3) # false
print('hello' in str_3) # true
print('hey' in str_3) # false









