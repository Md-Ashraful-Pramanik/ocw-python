# method => function
# attribute => variable

# model, color, brand, price, mileage
class Car:
    def __init__(self, model, color, price, mileage, brand="BMW"):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price
        self.mileage = mileage
    
    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Price: {self.price}"
    
    def start(self):
        print(f"{self.brand} Car is starting...")
        """
        statement
        """

# Encapsulation
a = Car(
    model="abc",
    color="red",
    price=45646546,
    mileage= "100km/hour",
)

print(a)
a.start()

a.start()
