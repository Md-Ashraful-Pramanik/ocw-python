def hello(name):
    print(f"Hello {name}")

def how_are_you(name):
    print(f"How are you {name}")

def see_you(name):
    print(f"See you {name}")

def greeting(greet, name):
    greet(name)

greeting(hello, "Ashraful")
greeting(how_are_you, "Ashraful")
greeting(see_you, "Ashraful")

x = hello
x("Mr. x")

# inner function
def normal_func():
    def inner_function():
        print("Hello")
    
    inner_function()

normal_func()
