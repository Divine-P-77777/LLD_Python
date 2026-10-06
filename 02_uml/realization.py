# ## Realization

# Realization represents a relationship where a concrete
# class implements the contract defined by an interface
# (or abstract class).

# The interface defines WHAT should be done.

# The implementing class defines HOW it is done.


from abc import ABC, abstractmethod


class Loginable(ABC):

    @abstractmethod
    def login(self):
        pass


class User(Loginable):

    def login(self):
        print("User logged in")


class Admin(Loginable):

    def login(self):
        print("Admin logged in")


user = User()
admin = Admin()

user.login()
admin.login()



# ┌─────────────────────────┐
# │      <<interface>>      │
# │        Loginable        │
# ├─────────────────────────┤
# │ + login(): void         │
# └─────────────────────────┘
#              △
#              |
#              | - - - - - - - -
#              |  realization
#              | - - - - - - - -
#              |
# ┌─────────────────────────┐
# │          User           │
# ├─────────────────────────┤
# │ + login(): void         │
# └─────────────────────────┘