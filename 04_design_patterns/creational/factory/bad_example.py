from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing Burger")


class RestaurantService:
    def create_order(self, food_type: str):
        if food_type == "pizza":
            food = Pizza()
        elif food_type == "burger":
            food = Burger()
        else:
            print("Invalid food type")
            return None

        food.prepare()
        return food


# Client
restaurant = RestaurantService()
restaurant.create_order("pizza")

Problems:
1. Tight Coupling: RestaurantService directly depends on concrete food classes.
2. OCP Violation: Adding Pasta requires modifying RestaurantService.
3. Poor Maintainability: Object creation logic is mixed with business logic.
