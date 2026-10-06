# # Inheritance

# Inheritance allows a child class to acquire
# properties and methods of a parent class.

# Parent Class:
# Animal

# Child Class:
# Dog

# Relationship:

# Animal
#    ↓
#   Dog

# Dog IS-A Animal.

# ## What does Dog inherit?

# Dog automatically gets:

# - name
# - age
# - eat()
# - sleep()



class Animal:

    def __init__(self, name: str, age: int):
        print("Animal INIT")

        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")


class Dog(Animal):

    def __init__(
        self,
        name: str,
        age: int,
        breed: str
    ):
        super().__init__(name, age)  # call the parent class's __init__().

        print("This is dog init")

        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(
            f"Name is {self.name}, "
            f"age is {self.age}, "
            f"breed is {self.breed}"
        )




dog = Dog("Tommy", 3)

dog.bark()
dog.eat()
dog.sleep()
dog.display()



class Vehicle:

    def start(self):
        print("Vehicle starts")


class Car(Vehicle):

    def start(self):
        print("Car starts with key")


class Bike(Vehicle):

    def start(self):
        print("Bike starts with button")


bike = Bike()
bike.start()        
# Vehicle.start()
#        ↓
# overridden by
#        ↓
# Car.start()
# Bike.start()