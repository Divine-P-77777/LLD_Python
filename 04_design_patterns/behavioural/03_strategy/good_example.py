from abc import ABC, abstractmethod


# 1. Strategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass


# 2. Concrete strategies
class DiwaliDiscount(DiscountStrategy):

    def calculate_discount(self, amount: float) -> float:
        return amount * 0.20


class HoliDiscount(DiscountStrategy):

    def calculate_discount(self, amount: float) -> float:
        return amount * 0.15


class RepublicDayDiscount(DiscountStrategy):

    def calculate_discount(self, amount: float) -> float:
        return amount * 0.10


class MonsoonDiscount(DiscountStrategy):

    def calculate_discount(self, amount: float) -> float:
        return amount * 0.25


# 3. Context: uses a strategy without knowing its details
class DiscountService:

    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        return self.strategy.calculate_discount(amount)


# 4. Client code
if __name__ == "__main__":
    amount = 1000

    strategies = {
        "Diwali": DiwaliDiscount(),
        "Holi": HoliDiscount(),
        "Republic Day": RepublicDayDiscount(),
        "Monsoon": MonsoonDiscount(),
    }

    for festival, strategy in strategies.items():
        service = DiscountService(strategy)
        discount = service.calculate_discount(amount)
        final_price = amount - discount

        print(
            f"{festival}: Discount = ₹{discount:.2f}, "
            f"Final Price = ₹{final_price:.2f}"
        )
