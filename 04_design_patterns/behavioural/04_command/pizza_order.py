# concreate command
from order import Order


class PizzaOrder(Order):
    def __init__(self, chef):
        self._chef = chef

    def execute(self):
        self._chef.cook_pizza()
