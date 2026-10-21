from weather_station import WeatherStation
from phone_display import PhoneDisplay
from tv import TV


station = WeatherStation()

phone = PhoneDisplay()
tv = TV()

# Subscribe observers
station.add_observer(phone)
station.add_observer(tv)

# Notify all observers
station.update_temperature(25.5)

print("--- Remove TV ---")

# Unsubscribe TV
station.remove_observer(tv)

# Only phone receives the update
station.update_temperature(30.0)