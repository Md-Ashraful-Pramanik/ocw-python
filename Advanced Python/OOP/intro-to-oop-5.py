# method => function
# attribute => variable

# model, color, brand, price, mileage
class Car:
    def __init__(
            self, 
            model, 
            color, 
            price, 
            making_price,
            mileage, 
            brand="BMW"
        ):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price
        self.mileage = mileage
        self.__making_price = making_price # private property
    
    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Price: {self.price}"
    
    def start(self):
        print(f"{self.brand} Car is starting...")
        """
        statement
        """
    
    def get_making_price(self):
        return self.__making_price

# Encapsulation
a = Car(
    model="abc",
    color="red",
    price=45646546,
    mileage= "100km/hour",
    making_price=4000000,
)

print(a)
# print(a.__making_price)
print(a.get_making_price())

print(a.__dict__) # show all the property and value
print(a._Car__making_price) # private _<ClassName><PrivatePropertyName>

print(a.__dict__.keys())
print(a.__dict__.values())

a.damage_amount = 50

print(a.damage_amount)

print(a.__dict__.keys())