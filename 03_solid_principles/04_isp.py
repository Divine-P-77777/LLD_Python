# I - Interface Segregation Principle
# Definition: The Interface Segregation Principle ensures that classes are not forced to implement methods they don't need.

# Simple terms:
# Break large, general-purpose interfaces into smaller, more specific ones.

# Benefits:
# Maintainability - Code is easier to maintain and update
# Flexibility - Classes can pick and choose what they need
# Testability - Easier to test because classes have only

# what they need
# Key Rule
# : Classes should only depend on the methods they actually use.



#Bad Examples 

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass


class Worker(Employee):

    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Worker is working")


class Robot(Employee):

    def work(self):
        print("Robot is working")

    def eat(self):
        raise Exception("Robot can't eat")


worker = Worker()
worker.eat()
worker.work()

robot = Robot()
robot.work()
robot.eat()       # ❌ Exception


# Good Example

from abc import ABC, abstractmethod


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("Worker is working")

    def eat(self):
        print("Worker is eating")


class Robot(Workable):

    def work(self):
        print("Robot is working")


worker = Worker()

worker.work()
worker.eat()


robot = Robot()

robot.work()