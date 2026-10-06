# # __init__

# __init__ is called automatically when an object is created.

# user = User("Dipu", "...")

# Python internally initializes the object using __init__.

# # self

# self refers to the current object.

# self.name
# self.email

# Different objects have different instance state.

# user1.name
# user2.name

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)


user = User("Dipu", "dipu@example.com")

user.display()


# Interview point
# self is NOT a keyword.

# It is a conventional name for the reference to the current object.
