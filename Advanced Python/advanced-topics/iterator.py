my_list = [1, 5, 6, 8]

# List, tuple

iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

my_tuple = (5, 6, 5)
iterator = iter(my_tuple)
print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in range(10):
    print(i)

itertor = iter(range(10))

print(next(itertor))
print(next(itertor))
