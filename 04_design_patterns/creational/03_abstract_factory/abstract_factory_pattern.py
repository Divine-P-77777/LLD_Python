from abc import ABC, abstractmethod


# ==================================
# 1. ABSTRACT PRODUCTS
# ==================================

class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass


class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass


# ==================================
# 2. CONCRETE PRODUCTS
# ==================================

# North Indian Dishes

class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing Paneer Tikka")


class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken")


class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun")


# South Indian Dishes

class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada")


class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa")


class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam")


# Chinese Dishes

class SpringRolls(Starter):
    def prepare(self):
        print("Preparing Spring Rolls")


class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried Rice")


class FortuneCookie(Dessert):
    def prepare(self):
        print("Preparing Fortune Cookie")


# ==================================
# 3. ABSTRACT FACTORY
# ==================================

class CuisineFactory(ABC):

    @abstractmethod
    def create_starter(self) -> Starter:
        pass

    @abstractmethod
    def create_main_course(self) -> MainCourse:
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass


# ==================================
# 4. CONCRETE FACTORIES
# ==================================

class NorthIndianFactory(CuisineFactory):

    def create_starter(self):
        return PaneerTikka()

    def create_main_course(self):
        return ButterChicken()

    def create_dessert(self):
        return GulabJamun()


class SouthIndianFactory(CuisineFactory):

    def create_starter(self):
        return MeduVada()

    def create_main_course(self):
        return Dosa()

    def create_dessert(self):
        return Payasam()


class ChineseFactory(CuisineFactory):

    def create_starter(self):
        return SpringRolls()

    def create_main_course(self):
        return FriedRice()

    def create_dessert(self):
        return FortuneCookie()


# ==================================
# 5. CLIENT SERVICE / CONTEXT
# ==================================

class RestaurantService:

    def __init__(self, factory: CuisineFactory):
        self._factory = factory

    def change_cuisine(self, new_factory: CuisineFactory):
        self._factory = new_factory

    def create_meal(self):

        starter = self._factory.create_starter()
        main_course = self._factory.create_main_course()
        dessert = self._factory.create_dessert()

        starter.prepare()
        main_course.prepare()
        dessert.prepare()


# ==================================
# 6. CLIENT
# ==================================

restaurant = RestaurantService(NorthIndianFactory())

print("North Indian Meal:")
restaurant.create_meal()

print("\nSwitching Cuisine...\n")

restaurant.change_cuisine(ChineseFactory())

print("Chinese Meal:")
restaurant.create_meal()