# Accessing List Elements
a = [5, 6, 8]
print("List")
for el in a:
    print(el)

# Accessing Tuple Elements
a = (56, 93, 6)
print("Tuple")
for el in a:
    print(el)

# Accessing Set Elements
a = {6, 3, 5}
print("Set")
for el in a:
    print(el)

# Accessing Dictionary Elements
student = {
    "name": "Mr. A",
    "roll": 50,
    "class": 10,
    "phoneNumber": "015665846..",
    "address": "Puran Dhaka",
    "subjects": [
        "Bangla",
        "English",
        "Physics",
        "Chemistry",
        "Math",
        "Higher Math",
        "Biology"
    ]
}
print("Dictionary")
for el in student:
    print(el, student[el])

# Using range() function
# [0, 1, 2, 3, 4] 
print("Range")
print(list(range(-5, 30, -2)))
for i in range(2, 30, 2):
    print(i)

# Using enumerate() function
for index, element in enumerate(a):
    print(f"Index: {index} Value: {element}")
