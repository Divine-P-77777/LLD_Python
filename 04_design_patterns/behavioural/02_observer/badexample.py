class PhoneDisplay:

    def update(self, new_temp: float):
        print(f"Phone display temperature = {new_temp}")


class WeatherStation:

    def __init__(self):
        self._temperature = 0.0
        self._phone_display = PhoneDisplay()

    def update_temperature(self, new_temp: float):
        self._temperature = new_temp
        self._phone_display.update(self._temperature)


station = WeatherStation()
station.update_temperature(25.5)
station.update_temperature(30.0)




# Problem:
# - WeatherStation creates PhoneDisplay internally.
# - Adding a TV, laptop, or other display requires changing WeatherStation.
# - Displays cannot register or unregister independently.