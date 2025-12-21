# functions

name = input("What is your name?\n")
print("Hello", name)

print(int(3.14))

# create own custom functions
def hello():
    print('Hello World') 

hello()

def calculate_sum(a, b):
    print(a+b)

calculate_sum(3,1)

def calculate_sum(a, b):
    return(a+b)

sum = calculate_sum(5,5)
print(sum)


