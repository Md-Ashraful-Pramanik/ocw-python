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

print(student)

print(student["name"])
print(student["subjects"])
# print(student["results"])
# changing value stored under a key
student["name"] = "Mr. B"

print(student["name"])
print(student)

# delete a key value pair
del student["phoneNumber"]
print(student)

# Add new key value pair
student["age"] = 16
print(student)

# seeing dictionary key and value
print(list(student.keys()))
print(list(student.values()))

# adding new key value pair
student[5] = 500
print(student)

# Changing value of a key
student[5] = "abc"
print(student)

