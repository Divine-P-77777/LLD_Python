# SOLID
# L - Liskov Substitution Principle (LSP)
# Definition: It states that objects of a parent class should be replaceable with objects of a child class without breaking the program.
# Simple terms:
# If Child class is-a Parent class, then Child should work exactly like Parent
# You should be able to use Child class wherever Parent class is expected
# Child class should not break the behavior that Parent class promises
# No class should be forced to implement methods it doesn't use.
# Split large interfaces into smaller, more specific ones.


# Bad Example

from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, balance: int):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass


class SavingAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient balance")
        else:
            self.balance -= amount    

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Amount deposited, remaining balance: {self.balance}"
        )
class FixedDepositAccount(BankAccount):

    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        raise Exception("Cannot withdraw from FD")

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Amount deposited, remaining balance: {self.balance}"
        )


# Good Example :
from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, balance: int):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: int):
        pass


class WithdrawableAccount(BankAccount):

    @abstractmethod
    def withdraw(self, amount: int):
        pass


class SavingsAccount(WithdrawableAccount):

    def deposit(self, amount: int):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise Exception("Insufficient balance")

        self.balance -= amount
        print(f"Withdrawn: {amount}")


class FixedDepositAccount(BankAccount):

    def deposit(self, amount: int):
        self.balance += amount
        print(f"Deposited: {amount}")


# Usage

savings = SavingsAccount(1000)

savings.deposit(500)
savings.withdraw(300)

print(savings.balance)


fd = FixedDepositAccount(5000)

fd.deposit(1000)

print(fd.balance)        