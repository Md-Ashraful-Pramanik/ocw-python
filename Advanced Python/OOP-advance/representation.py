class Vector:
    def __init__(
            self,
            i,
            j,
            k
        ):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"({self.i}, {self.j}, {self.k})"

    def __repr__(self):
        return f"Vector(i={self.i}, j={self.j}, k={self.k})"

v = Vector(1, 2, 3)
print(v)
print(repr(v))
v2 = Vector(i=1, j=4, k=3)
print(repr(v2))
