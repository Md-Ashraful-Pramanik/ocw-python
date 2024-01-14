marks = [85, 60, 60, 80, 65, 70] # List or array 

print(marks)

# Accessing specific item from a list
print(marks[5]) # normal serial = index + 1
print(marks[-1])

# Accessing multiple element
print(marks[1:5])
print(marks[1:-1])
print(marks[1:0])


# Adding list item
# Append add one element at last
marks.append(50)
print(marks)

# insert item at the specified index
marks.insert(1, 90)
print(marks)


# Remove an item from list
marks.pop()
print(marks)

# Remove an item from list
marks.pop(4)
print(marks)

# removing using value
marks.remove(70)
print(marks)

# removing using value
marks.remove(60)
print(marks)

# marks.remove(5) # arise an error
del marks[1]
print(marks)


# default functions in list
print(len(marks))

marks.sort()
print(marks)

marks.clear()
print(marks)


# joining two list
a = [1, 5, 6, 10]
b = [9, 6, 3, 5]

print(a)
print(b)
# a.extend(b)
# print(a+b)
c = a+b
print(a)
print(b)
print(c)