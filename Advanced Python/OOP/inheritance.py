from abc import *
from typing import override

class Car:
    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
            brand,
            logo,
        ):
        self.model = model
        self.color = color
        self.price = price
        self.mileage = mileage
        self.brand = brand
        self.logo = logo
    
    def __str__(self) -> str:
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Price: {self.price}"

    def build_car(self):
        print("Car is building")


class BMWCar(Car): # child(parent)
    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
            logo="BMW",
            brand="BMW",
        ):
        super().__init__(
            model=model,
            color=color,
            price=price,
            mileage=mileage,
            brand=brand,
            logo=logo
        )
    
    # function/method override
    @override
    def build_car(self):
        super().build_car()
        print("BMW car building process")
    

class ToyotaCar(Car):
    def __init__(
            self, 
            model, 
            color, 
            price, 
            mileage,
            logo="Toyota",
            brand="Toyota",
        ):
        super().__init__(
            model=model,
            color=color,
            price=price,
            mileage=mileage,
            brand=brand,
            logo=logo
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

toyotaCar.build_car()
bmwCar.build_car()
