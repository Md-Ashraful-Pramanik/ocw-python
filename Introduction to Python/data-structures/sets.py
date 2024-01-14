# {}
a = {50, 60, 70, 40, 50}

print(a)
print(type(a))
print(len(a))

# Adding existing element
a.add(50)
print(a)

# Adding non-existing element
a.add(100)
print(a)

# update a set from another set
b = {50, 80, 90}

a.update(b)
print(a)

# Remove an element
a.remove(50) # give error if element is absent
print(a)

a.discard(50) # does not give error if element is absent
print(a)

a.discard(50)
print(a)

a.pop() # randomly delete one element
print(a)

a.clear() #removes all
print(a)

a = {1, 2}
b = {1, 2}

print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(b.issuperset(a))

print(a == b)

print("Example of Difference")
c = a - b
c = a.difference(b)
print(a)
print(b)
print(c)

print("Example of Intersection")
c = a.intersection(b)
print(a)
print(b)
print(c)

print("Example of Union")
c = a.union(b)
print(a)
print(b)
print(c)

print("Example of Update")
a.update(b)
print(a)
print(b)
