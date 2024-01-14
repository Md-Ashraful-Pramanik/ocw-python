names = ["Ashraful", "Kamal", "Walid", "Rishad", "Pulok"]

# Example of enumerate
for index, name in enumerate(names):
    print(index)
    print(name)

print(list(enumerate(names)))

# Implementing enumerate using zip
indices = list(range(len(names)))
print(list(zip(indices, names)))
