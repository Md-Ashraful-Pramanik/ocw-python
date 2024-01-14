from dataclasses import dataclass, field

# frozen = True => we will not be allowed to change any value
# slots  = True => Do not permit to add any extra attribute
# eq     = False => Do not generate equal method (Default: True)
# order  = True => le, lt, gt, ge (Default: False)
@dataclass(order=True)
class Circle:
    sorting: float=field(init=False, repr=False)
    x: float 
    y: float 
    r: float # = field(repr=False)

    def __post_init__(self):
        assert type(self.x) == int or type(self.x) == float, "X coordinate of the circle should be number"
        assert type(self.y) == int or type(self.y) == float, "Y coordinate of the circle should be number"
        assert type(self.r) == int or type(self.r) == float, "Radius of the circle should be number"
        self.sorting = self.r
    
    def get_area(self):
        return 3.1416 * self.r * self.r


c1 = Circle(x=10, y=20, r='5')

# assert condition, error_msg