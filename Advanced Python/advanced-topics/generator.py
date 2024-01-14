# even number generator
# 2, 4, 6 ...

# generator => return each time when we give next
# normal => return only once

def even_number():
    number = 2
    while True:
        yield number
        number += 2

even_number_generator = even_number()

print(next(even_number_generator))
print(next(even_number_generator))
print(next(even_number_generator))
print(next(even_number_generator))