## 4. Association

# Association represents a general relationship
# between two classes.

# It means objects of one class know about,
# communicate with, or interact with objects
# of another class.

# Example:

# A User places an Order.

# User ───────── Order

class Order:
    pass


class User:

    def place_order(self, order: Order):
        pass

# ┌──────────────┐              ┌──────────────┐
# │     User     │──────────────│    Order     │
# └──────────────┘   places     └──────────────┘


## 5. Inheritance

## Inheritance

# Inheritance represents an "IS-A" relationship.

# A child class inherits attributes and methods
# from a parent class.

# Example:

# Dog IS-A Animal
class Animal:

    def eat(self):
        pass


class Dog(Animal):

    def bark(self):
        pass
# ┌──────────────────┐
# │     Animal       │
# ├──────────────────┤
# │ + eat(): void    │
# └──────────────────┘
#           △          
#           │
#           │
# ┌──────────────────┐
# │       Dog        │
# ├──────────────────┤
# │ + bark(): void   │
# └──────────────────┘        

# 6. Hollow triangle points toward the parent.

## Composition

# Composition represents a strong HAS-A relationship.

# One object is composed of another object.

# The contained object strongly depends on
# the lifetime of the owner.

# Example:

# Car HAS-A Engine.

# If the Car is destroyed, its Engine
# is considered part of that Car and
# does not have an independent lifecycle
# in the model.

class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

# ┌──────────────┐
# │     Car      │
# └──────────────┘
#        ◆
#        │
#        │
# ┌──────────────┐
# │    Engine    │
# └──────────────┘

# Filled diamond = Composition


## 7. Aggregation

# Aggregation represents a weaker HAS-A relationship.

# One object contains/references another object,
# but the contained object can exist independently.

# Example:

# Classroom HAS Students.

# If the Classroom is removed,
# the Students still exist.


class Student:

    def __init__(self, name):
        self.name = name


class Classroom:

    def __init__(self, students):
        self.students = students

student1 = Student("A")
student2 = Student("B")

students = [student1, student2]

classroom = Classroom(students)

# ┌──────────────────┐
# │    Classroom     │
# └──────────────────┘
#         ◇
#         │
#         │
# ┌──────────────────┐
# │     Student      │
# └──────────────────┘

# # Hollow diamond = Aggregation

#                     UML RELATIONSHIPS
#                            │
#         ┌──────────────────┼──────────────────┐
#         │                  │                  │
#         ▼                  ▼                  ▼
#    Association        Inheritance          HAS-A
#                                              │
#                                       ┌──────┴──────┐
#                                       │             │
#                                       ▼             ▼
#                                  Composition   Aggregation
#                                  Strong HAS-A   Weak HAS-A