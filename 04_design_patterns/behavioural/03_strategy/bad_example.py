
# bad_example.py

class DiscountService:
    def calculate_discount(self, festival, amount):
        if festival == "diwali":
            return amount * 0.20

        elif festival == "holi":
            return amount * 0.15

        elif festival == "republic_day":
            return amount * 0.10

        elif festival == "monsoon":
            return amount * 0.25

        else:
            return 0.0


if __name__ == "__main__":
    service = DiscountService()

    amount = 1000

    print("Diwali discount:", service.calculate_discount("diwali", amount))
    print("Holi discount:", service.calculate_discount("holi", amount))
    print("Republic Day discount:",
          service.calculate_discount("republic_day", amount))
    print("Monsoon discount:",
          service.calculate_discount("monsoon", amount))




# Why is this bad?
# 1. All discount calculations are inside one class.
# 2. Every new festival requires another conditional branch.
# 3. A change to one discount risks affecting existing logic.
# 4. Testing one discount independently is less convenient.