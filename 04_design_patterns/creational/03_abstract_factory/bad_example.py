from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


# North Indian
class PaneerTikka(Food):
    def prepare(self):
        print("Preparing Paneer Tikka")


class ButterChicken(Food):
    def prepare(self):
        print("Preparing Butter Chicken")


class GulabJamun(Food):
    def prepare(self):
        print("Preparing Gulab Jamun")


# South Indian
class MeduVada(Food):
    def prepare(self):
        print("Preparing Medu Vada")


class Dosa(Food):
    def prepare(self):
        print("Preparing Dosa")


class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam")


# Chinese
class SpringRolls(Food):
    def prepare(self):
        print("Preparing Spring Rolls")


class FriedRice(Food):
    def prepare(self):
        print("Preparing Fried Rice")


class FortuneCookie(Food):
    def prepare(self):
        print("Preparing Fortune Cookie")


# Client Service
class RestaurantService:

    def create_meal(self, cuisine_type: str):

        if cuisine_type == "north_indian":
            starter = PaneerTikka()
            main_course = ButterChicken()
            dessert = GulabJamun()

        elif cuisine_type == "south_indian":
            starter = MeduVada()
            main_course = Dosa()
            dessert = Payasam()

        elif cuisine_type == "chinese":
            starter = SpringRolls()
            main_course = FriedRice()
            dessert = FortuneCookie()

        else:
            raise ValueError("Cuisine not available")

        starter.prepare()
        main_course.prepare()
        dessert.prepare()


# Client
restaurant = RestaurantService()
restaurant.create_meal("north_indian")