import numpy as np

# Numpy array
a = [
    [1, 5], 
    [2, 57], 
    [3, 96]
]

numpy_array = np.array(a)
print(numpy_array)
print(numpy_array.shape)

# Numpy array creation
## All zero
print(np.zeros((4, 5)))
print(np.zeros((4, 5), dtype=int))

## All one
print(np.ones((4, 5), dtype=int))

## Identity matrix
print(np.eye(3))

print(np.ones((4, 5)) * 5)

## taking random data
print(np.random.random((3,3)))

# Data types in numpy
# np.int
# np.float
# np.complex 
# np.bool

# Type conversion
a = np.random.random((3,3))*50
print(a)
a = a.astype(int)
print(a)

# View Data type
print(a.dtype)

# Operations in numpy
a = np.random.random((3,3)) * 10
b = np.random.random((3,3)) * 10

print(a + b) # element-wise addition
print(a - b) # element-wise subtraction
print(a * b) # element-wise product
print(a / b) # element-wise division
print(a @ b) # matrix multiplication
print(a ** 2) # element-wise power

print(np.exp(a))  # element-wise e^
print(np.log(a))  # element-wise log
print(np.sqrt(a)) # element-wise sqaure root
print(np.sin(a))  # element-wise sin
print(np.cos(a))  # element-wise cos

# dot product (vector)
a = np.random.random((3,))
b = np.random.random((3,))

print(a.dot(b))
print(a[0] * b[0] + a[1] * b[1] + a[2] * b[2])

# Relational operator
print(a == b)
print(a > b)

# Aggregate function
print("Aggregate")
a = np.random.random((3, 2)) * 50
a = a.astype(int)

print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.min(axis=0))
print(a.max(axis=0))
print(a.mean())

print(a.cumsum(axis=0))
print(a.cumsum(axis=1))

print(np.std(a))

a.sort(axis=0)
print(a)

a.sort(axis=1)
print(a)

print(a.T)

# Change shape
a.resize((1, 6))
print(a)

a.resize((2, 3))
print(a)

a= np.random.random((5, 6))
a.resize((5, 3, 2))
print(a)

print(a.ravel())

# Combining
a = np.random.random((3, 2))
b = np.random.random((3, 2))

print(np.vstack((a, b))) # column should be same
print(np.hstack((a, b))) # row should be same

# slicing
print(a[:, 0])

# Copy
b = a
b[0, 0] = 50
print(a)
print(b)

# Broadcasting
a = np.random.random((2, 2))
b = np.random.random((1, 2))

print(a)
print(b)
print(a * b)
print(a * np.vstack((b, b)))

# Splitting
a = np.random.random((6, 4))
print(a)
print(np.vsplit(a, 2))

print(a)
print(np.hsplit(a, 2))
