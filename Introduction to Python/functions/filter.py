# Problem 1: Filter positive numbers from a list
a = [5, 6, -5, 10, -5]
## first way using for loop
positive_numbers = []
for el in a:
    if el > 0:
        positive_numbers.append(el)
print(positive_numbers)

## second way using filter and normal function
def is_positive(num):
    return num > 0  # function's return type should be boolean

positive_numbers = list(filter(is_positive, a))
print(positive_numbers)

## third way using filter and lambda function
positive_numbers = list(filter(lambda num: num > 0, a))
print(positive_numbers)

## In similar way we can filter negative numbers from a list
negative_numbers = list(filter(lambda num: num < 0, a))
print(negative_numbers)

# Problem 2: Filter names which contains character 'a' from a list
names = ["Ashraful", "Kamal", "Walid", "Rishad", "Pulok"]
names_with_char_a = list(filter(lambda name: 'a' in name.lower(), names))
print(names_with_char_a)
