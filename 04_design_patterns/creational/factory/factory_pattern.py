# 3. Solution – Factory Pattern
# The Factory Pattern centralizes object creation in a separate Factory class.

# Instead of creating objects directly, the client requests an object from the factory.


from abc import ABC, abstractmethod


# Product Interface
class Food(ABC):

    @abstractmethod
    def prepare(self):
        pass


# Concrete Products
class Pizza(Food):

    def prepare(self):
        print("Preparing Pizza")


class Burger(Food):

    def prepare(self):
        print("Preparing Burger")


# Factory
class FoodFactory:

    @staticmethod
    def create_food(food_type: str) -> Food:

        if food_type == "pizza":
            return Pizza()

        elif food_type == "burger":
            return Burger()

        raise ValueError("Invalid food type")


# Client Service
class RestaurantService:

    def create_order(self, food_type: str):
        food = FoodFactory.create_food(food_type)
        food.prepare()
        return food


# Client
restaurant_service = RestaurantService()

restaurant_service.create_order("pizza")
restaurant_service.create_order("burger")