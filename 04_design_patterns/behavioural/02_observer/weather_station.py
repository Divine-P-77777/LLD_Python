from observer import Observer


class WeatherStation:

    def __init__(self):
        self._temperature = 0.0
        self._observers: list[Observer] = []

    def add_observer(self, new_observer: Observer):
        if new_observer not in self._observers:
            self._observers.append(new_observer)

    def remove_observer(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def update_temperature(self, new_temp: float):
        self._temperature = new_temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers.copy():
            observer.update(self._temperature)