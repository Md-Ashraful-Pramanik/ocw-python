def square(x):
    return x **2 

print(square(2))


def add(a, b):
    return a+b

def minus(a, b):
    return a-b


print(add(10, 15))
print(minus(10, 5))

print(minus(5, 10))

# example of keyword arguments
print(minus(b=500, a=5000))

# default value in parameter
def minus(b, a=50): 
    return a-b

print(minus(50))

print(add(a=50, b=5000))

