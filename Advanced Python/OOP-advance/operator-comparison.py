# >, >=, <, <=, ==

class Circle:
    def __init__(
        self,
        x, 
        y,
        r,
    ) -> None:
        self.x = x
        self.y = y
        self.r = r
    
    def get_area(self):
        return 3.1416 * self.r * self.r
    
    def __eq__(self, other) -> bool:
        return self.r == other.r

    def __lt__(self, other):
        return self.r < other.r

    def __gt__(self, other):
        return self.r > other.r
    
    def __le__(self, other):
        return self.r <= other.r
    
    def __ge__(self, other):
        return self.r >= other.r
    
    def __str__(self):
        return f"Center: ({self.x}, {self.y}), Radius: {self.r}"
    
    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, r={self.r})"
    
c1 = Circle(x=0, y=0, r=5)
print(c1)

c2 = Circle(x=5, y=2, r=5)
print(c2)

print(c1 == c2)

c3 = Circle(x=5, y=2, r=10)
print(c1 < c3)
print(c2 < c3)
