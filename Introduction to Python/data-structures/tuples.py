a  = [5, 8, 6, 6]
print(a)
a[0] = 50
print(a)

a = (5, 6, 6, 78, 63) # intialization requires ()

# Tuple : constant
print(a)
print(a[1])
print(a[1:5])
print(a[-1])

print(a)

b = list(a)
print(b)
b[0] = 5000
print(b)

c = tuple(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

