# scope - when can you access a variable

# local scope - defined in a function or class
# enclosing - defined in enclosing or nested function
# global - defiend at the top level of the module or file
# built-in scope - refers to python's built-in functions, modules, and keywords (e.g. str, type, isinstance)

# local
def func():
    var = 10 # locally scoped to func
    print(var)

func()

def outer_func():
    msg = "Hello!"

    def inner_func():
        res = "How are you?" # outer func cannot access this
        print(msg) # inner func can access msg

    inner_func()

outer_func()

def outer_func2():
    msg = "Hola!"
    res = "" # declare res

    def inner_func2():
        nonlocal res 
        res = "How are you?" # allow modification of an enclosing variable
        print(msg) # inner func can access msg

    inner_func2()
    print(res)

outer_func2()

var = 100

def show_var():
    print(var)

show_var()

def show_var2():
    global var_2
    var_2 = 10
    print(var)
    print(var_2)

show_var2()
print(var_2)

