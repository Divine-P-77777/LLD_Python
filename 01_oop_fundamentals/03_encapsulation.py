# Encapsulation

# Encapsulation means bundling:

#     Data + Methods

# inside a class while controlling how the internal state is accessed.

# Goal:

# Protect object state from invalid/uncontrolled modification.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance  # balance is  a private attribute using the __(dunder)

    def __isServerLive(self):   # isServerLive is Private method
            return True        

    def deposit(self, amount):
        if self.__isServerLive() == True:
            self.__balance += amount
            print(f"Amount added ,current balance {self.__balance}")
        else:
            print("Server is Down")    

    

    def withdraw(self, amount):

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount

    # Getter
    def get_balance(self):
        return self.__balance
    
    #Setter
    def set_balance(self,new_amount):
        self.__balance = new_amount
        
    # mostly we define the getter and setter for  a private attribute

account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance())


# Note: Don't allow every part of the system to directly modify important object state.
# Expose controlled methods instead.
