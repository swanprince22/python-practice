# conditional statements and logical operators

print(3!=4)

age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

is_citizen = True

print(is_citizen and age)

print(age or is_citizen)

print(not "Hello")