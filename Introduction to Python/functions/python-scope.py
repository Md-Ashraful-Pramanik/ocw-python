# Access/Read global variable  => Nothing to do
# Modify/Write global variable => `global variableName`

def example_func():
    x = 10 # local variable

print(x) # local variable will not work in global scope


x = 10 # global variable

def example_func():
    global x 
    print(x) # global variable can be accessed inside function scope 
    x = 50

example_func()
print(x)

x = 10 # global variable

def example_func_1():
    global x 
    print(x) # global variable can be accessed inside function scope 
    x = 50
    y = 100 # Function Local variable
    print(y)

def example_func_2():
    # print(y) # y is not defined in this scope so it will throw error
    print(x) # global variable can be accessed inside function scope 

example_func_1()
example_func_2()

