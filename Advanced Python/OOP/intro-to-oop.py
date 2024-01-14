# model, color, brand, price, mileage
class Car:
    def __init__(self):
        self.model = None
        self.color = None
        self.brand = None
        self.price = None
        self.mileage = None

# Encapsulation
a = Car()

a.model = "abc"
a.color = "red"
a.brand = "Toyota"
a.price = 45646546
a.mileage = "100km/hour"


print(f"Brand: {a.brand}, Model: {a.model}, Color: {a.color}, Price: {a.price}, Mileage: {a.mileage}")
