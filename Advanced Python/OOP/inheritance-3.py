from abc import *
from typing import override

# Abstract class
class Car(ABC):
    brand = None
    logo = None

    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
        ):
        self.model = model
        self.color = color
        self.price = price
        self.mileage = mileage
    
    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Price: {self.price}"

    @abstractmethod
    def build_car(self):
        pass


class BMWCar(Car): # child(parent)
    logo="BMW"
    brand="BMW"

    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
        ):
        super().__init__(
            model=model,
            color=color,
            price=price,
            mileage=mileage,
        )
    
    # function/method override
    @override
    def build_car(self):
        print("BMW car building process")
    

class ToyotaCar(Car):
    logo="Toyota"
    brand="Toyota"

    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
        ):
        super().__init__(
            model=model,
            color=color,
            price=price,
            mileage=mileage,
        )
    
    def build_car(self):
        print("Toyota car building process")


toyotaCar = ToyotaCar(
    model="Toyota ABC",
    color="red",
    price=100000,
    mileage="60km/hour"
)

bmwCar = BMWCar(
    model="BMW ABC",
    color="red",
    price=500000,
    mileage="100km/hour"
)

print(toyotaCar)
print(bmwCar)

print(toyotaCar.brand)
print(bmwCar.brand)

print(ToyotaCar.brand)
print(BMWCar.brand)

print(toyotaCar.__dict__.keys())

toyotaCar2 = ToyotaCar(
    model="Toyota ABC 2",
    color="red",
    price=200000,
    mileage="60km/hour"
)

print(toyotaCar2.brand)
print(toyotaCar2.__dict__.keys())

ToyotaCar.brand = "Toyota 2"
print(toyotaCar.brand)
print(toyotaCar2.brand)

