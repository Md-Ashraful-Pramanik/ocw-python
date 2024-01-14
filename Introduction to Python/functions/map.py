# Problem - 1: Find the length of each name in a list of names
names = ["Ashraful", "Kamal", "Walid", "Rishad", "Pulok"]

## First way using normal for loop
name_lens = []
for name in names:
    name_lens.append(len(name))
print(name_lens)

## Second way using map
name_lens = list(map(len, names))
print(name_lens)

# Problem - 2: Find the full name of each person from two lists of first and last names
first_names = ["Md.", "Mr.", "Md.", "GM", "Fardin"]
last_names = ["Ashraful", "Kamal", "Walid", "Rishad", "Pulok"]

## first way using normal for loop
full_names = []
for i in range(len(first_names)):
    full_names.append(f'{first_names[i]} {last_names[i]}')
print(full_names)

## second way using zip and loop
full_names = []
for zipped_name in zip(first_names, last_names):
    print(zipped_name)
    first_name, last_name = zipped_name
    full_names.append(f'{first_name} {last_name}')
print(full_names)

## third way using zip and loop
full_names = []
for first_name, last_name in zip(first_names, last_names):
    full_names.append(f'{first_name} {last_name}')
print(full_names)

## fourth way using zip and map
def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}'

full_names = list(map(get_full_name, zip(first_names, last_names)))
print(full_names)

## fifth way using map, zip and lambda
full_names = list(map(lambda name: f'{name[0]} {name[1]}', zip(first_names, last_names)))
print(full_names)

## sixth way using map and lambda
full_names = list(map(lambda first_name, last_name: f'{first_name} {last_name}', first_names, last_names))
print(full_names)

# Problem - 3: Find the square of each number in a list of numbers
a = [5, 89, 3, 46]

## using map and lambda
square_a = list(map(lambda x: x**2, a))

print(square_a)
