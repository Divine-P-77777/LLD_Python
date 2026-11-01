# O - Open Close Principle (OCP)
# Definition: Software entities (classes, modules, functions) should be open for extension but closed for modification.
# Simple terms:
# Open for extension = You can add new features easily
# Closed for modification = Don't change existing working code
# Example: Adding new payment methods (Credit Card, UPI, PayPal) without modifying the existing payment processing code.


# Bad Examples:
class PaymentProcessor:
    def pay(self,payment_method:str,amount:int):
        if payment_method == "UPI":

            if payment_method == "UPI":
                print(f"Starting UPI transaction of Rs. {amount}")
                print("UPI transaction finished")
            elif payment_method == "credit_card":
                print(f"Starting credit card transaction of Rs. {amount}")
                print("Credit card transaction finished")
            elif payment_method == "UPI":
                print(f"Starting UPI transaction of Rs. {amount}")
                print("UPI transaction finished")

pay_p = PaymentProcessor()                
pay_p.pay("credit_card",500)
# suppos  now I  want paypal then I have to modify the class method which violates OCP

# Good Examples :

from abc import  ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount:int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying via upi of Rs.{amount}")    


class DebitCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying via debit card of Rs.{amount}")    

class CreditCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying via credit card of Rs.{amount}")    

class PaypalPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying via paypal of Rs.{amount}")    


class paymentProcessor:
    def process_payment(self,payment_method:PaymentMethod,amount:int):
        payment_method.pay(amount)


debit = DebitCardPayment()
credit = CreditCardPayment()
paypal = PaypalPayment()

paym_process = paymentProcessor()

paym_process.process_payment(debit,500)
paym_process.process_payment(paypal,2500)
