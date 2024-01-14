from pydantic import BaseModel

class Circle(BaseModel):
    x: float
    y: float
    r: float

c = Circle(x=10, y='20', r=1)
print(c)