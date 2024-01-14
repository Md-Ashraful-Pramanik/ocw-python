"""
### Mobile Shop
Suppose you are an owner of a mobile shop where you sell Samsung, Vivo, Oppo, iPhone. Every phone has brand, model, buying price, selling price, RAM, Storage as property and send message, initiate a call, turn on bluetooth, turn on wifi as method. You can assume turn on bluetooth and wifi is same for all the devices but send message and initiate call is different in every phones. 
Now, implement this shop using OOP concept.
"""

from abc import *
from typing import *

class Phone(ABC):
   brand = None
   def __init__(
         self,
         model, 
         buying_price, 
         selling_price, 
         RAM, 
         storage
      ):
      self.model = model
      self.__buying_price = buying_price
      self.selling_price = selling_price
      self.RAM = RAM
      self.storage = storage
   
   def turn_on_bluetooth(self):
      print("Turning bluetooth...")
   
   def turn_on_wifi(self):
      print("Turning wifi...")

   @abstractmethod
   def send_message(self):
      pass

   @abstractmethod
   def initiate_call(self):
      pass

   def get_buying_price(self):
      return self.__buying_price

   def set_buying_price(self, buying_price):
      self.__buying_price = buying_price

   def __str__(self):
      return f"Brand: {self.brand}, Model: {self.model}, Selling Price: {self.selling_price}, RAM: {self.RAM}, Storage: {self.storage}"
   
class Samsung(Phone):
   brand = "Samsung"
   @override
   def send_message(self):
      print("Sending message from samsung phone")
   
   @override
   def initiate_call(self):
      print("Initiating call from samsung phone")
   
class Vivo(Phone):
   brand = "Vivo"

   @override
   def send_message(self):
      print("Sending message from Vivo phone")

   @override
   def initiate_call(self):
      print("Initiating call from Vivo phone")

class Oppo(Phone):
   brand = "Oppo"
   def send_message(self):
      print("Sending message from Oppo phone")

   def initiate_call(self):
      print("Initiating call from Oppo phone")

class iPhone(Phone):
   brand = "iPhone"
   def send_message(self):
      print("Sending message from iPhone phone")

   def initiate_call(self):
      print("Initiating call from iPhone phone")


class MobileShop:
   def __init__(self):
      self.phones = []
   
   def add_phone(self, phone):
      self.phones.append(phone)
   
   def show_phones(self):
      for phone in self.phones:
         print(phone)
   
   @staticmethod
   def show_ad():
      print("Showing advertisement for this mobile shop.")

my_shop = MobileShop()
my_shop.add_phone(Samsung("A52", 30000, 35000, 8, 128))
my_shop.add_phone(Vivo("X", 10000, 12000, 4, 64))
my_shop.add_phone(Oppo("A", 20000, 22000, 6, 64))
my_shop.add_phone(iPhone("14", 200000, 220000, 4, 128))

my_shop.show_phones()
MobileShop.show_ad()
my_shop.show_ad()
