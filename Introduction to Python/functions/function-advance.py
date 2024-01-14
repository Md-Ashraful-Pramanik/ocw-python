# first name and last name => fullname
def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}'

my_name = get_full_name('Md.', 'Ashraful')
print(my_name)

# keyword argument
print(get_full_name(last_name='Ashraful', first_name='Md.'))

# default value in parameter or input
def get_full_name(first_name='Md.', last_name='Ashraful'):
    return f'{first_name} {last_name}'

print(get_full_name())
print(get_full_name(last_name='Kamal', first_name='Mr.'))

# arbitrary arguments (*)
def calculate_sum(*a):
    sum = 0
    for el in a:
        sum = sum + el
    return sum

print(calculate_sum(50, 90, 60, 70, 80, 10, 20))

# keyword arbitrary arguments (**)
def example_kw_ar_arg(**a):
    print(type(a))
    print(a)

example_kw_ar_arg(first_name='Mr.', last_name='Ashraful', age=26)

# Passing list as parameter
def calculate_sum(a):
    sum = 0
    for el in a:
        sum = sum + el
    return sum

print(calculate_sum([50, 60]))

# what happens when function does not return anything
output = example_kw_ar_arg(first_name='Mr.', last_name='Ashraful', age=26)
print(f"output of function: {output}")

# multiple outputs from function
def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}', f'{first_name.capitalize()} {last_name.capitalize()}'

original_name, capitalized_name = get_full_name('mr.', 'abc')
print(original_name, capitalized_name)


print(5, 6, 46, 79465, 46)