## Class

# A class is a blueprint/template for creating objects.

## Object

# An object is an instance of a class.

# Example:

# Car → class
# car1 → object
# car2 → object

# ## State

# Data stored inside an object.

# Example:
# brand
# model

# ## Behavior

# Actions performed by an object.

# Example:
# start()

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started")


# Objects
car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

car1.start()
car2.start()



class Employee:

    company = "ABC"       # Class attribute

    def __init__(self, name, salary):
        self.name = name      # Instance attribute
        self.salary = salary


e1 = Employee("A", 50000)
e2 = Employee("B", 60000)

print(e1.name)
print(e2.name)

print(e1.company)
print(e2.company)


# Remember
# Class attribute
#     ↓
# Shared by objects

# Instance attribute
#     ↓
# Belongs to individual object