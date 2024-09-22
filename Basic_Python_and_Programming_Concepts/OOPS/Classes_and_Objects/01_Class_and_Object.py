class Car:
    # Class attributes
    wheels = 4

    # Constructor
    def __init__(self, brand, model):
        # Instance Variables
        self.brand = brand
        self.model = model

    def honk(self):
        print("Beep Beep")

# Creating objects
car1 = Car("TATA", "Nexon")  # 'car1' is an object of the Car class
car2 = Car("Mahindra", "XUV700")

# Accessing attributes, class variables and methods
print(car1.brand) # Accessing and attribute
print(car2.wheels) # Accessing a class variable
car1.honk() # Calling a method
