

# Basic Elements

## 1. Class

# A class is a blueprint/template for creating objects.

# It contains:

# - Attributes → data/state
# - Methods → behavior/actions

# Example:

class User:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def login(self):
        pass


# UML:

# ┌──────────────────────┐
# │        User          │
# ├──────────────────────┤
# │ - name: str          │
# │ - age: int           │
# ├──────────────────────┤
# │ + login(): void      │
# └──────────────────────┘



#      +  Public
#      -  Private
#      #  Protected
#      ~  Package/Internal

## 2. Interface

# An interface defines what a class must do,
# but not how it does it.

# Python does not have a separate `interface` keyword.

# We commonly use an Abstract Base Class (ABC)
# to represent an interface-like contract.

# Example:
from abc import ABC, abstractmethod


class Loginable(ABC):

    @abstractmethod
    def login(self):
        pass

class User(Loginable):

    def login(self):
        print("User logged in")

# ┌─────────────────────────┐
# │      <<interface>>      │
# │        Loginable        │
# ├─────────────────────────┤
# │ + login(): void         │
# └─────────────────────────┘
#              △
#              │
#              │ implements
#              │
# ┌─────────────────────────┐
# │          User           │
# ├─────────────────────────┤
# │ - name: str             │
# │ - age: int              │
# ├─────────────────────────┤
# │ + login(): void         │
# └─────────────────────────┘                



## 3. Object
# An object is a real instance of a class created
# when the program runs.
# Class = Blueprint
# Object = Actual instance
# Example:
user1 = User("Anirudh", 25)
# Here:
# User  → Class
# user1 → Object


### Relationship

        #      CLASS
        #        │
        #        │ creates
        #        ▼
        # ┌──────────────┐
        # │     User     │
        # └──────────────┘
        #      │
        #      │ instance
        #      ▼
        # ┌──────────────┐
        # │    user1     │
        # │──────────────│
        # │ Anirudh      │
        # │ 25           │
        # └──────────────┘