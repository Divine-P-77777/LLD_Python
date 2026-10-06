# Abstraction is about reducing complexity. You expose only the necessary details to the user and hide all the complicated internal logic. The user doesn't need to know how things work inside, just that they work.

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CashfreePayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cashfree")


class StripePayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Stripe")


payment = CashfreePayment()

payment.pay(1000)

# Abstraction

# Expose what an object can do
# while hiding how it does it.

# Example:

# payment.pay(1000)

# The caller doesn't need to know:

# - API calls
# - authentication
# - HTTP requests
# - retries
# - payment provider internals
