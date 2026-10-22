
class Chef:
    def cook_pasta(self):
        print("Chef is cooking pasta")

    def cook_pizza(self):
        print("Chef is cooking pizza")


class Waiter:
    def __init__(self, chef: Chef):
        self._chef = chef

    def place_order(self, item: str):
        if item == "pasta":
            self._chef.cook_pasta()
        elif item == "pizza":
            self._chef.cook_pizza()
        else:
            print("Cannot take order")


chef = Chef()
waiter = Waiter(chef)

waiter.place_order("pasta")
waiter.place_order("pizza")
waiter.place_order("burger")


# Problems:
# - Waiter is tightly coupled to Chef.
# - Uses if-elif conditions for every order.
# - Adding new items requires modifying the Waiter class.
# - Violates the Open/Closed Principle.
# - Difficult to extend and maintain.