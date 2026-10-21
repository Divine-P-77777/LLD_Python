from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, new_temp: float):
        pass