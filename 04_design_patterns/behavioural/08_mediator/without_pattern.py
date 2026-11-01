class Airplane:
    def __init__(self,flight_number: str):
        self.__flight_number = flight_number

    def send_message(self,msg, airplane:"Airplane"):
        print(f"{self.__flight_number} is sending {msg} to {airplane.get_flight_no} ")

    def get_flight_no(self):
        return self.__flight_number


spicejet =Airplane ("Spice-45454")
indigo = Airplane("IND-5411")
air_india =  Airplane ("AIR-11231")

spicejet.send_message("Landing on runway 1",indigo)
spicejet.send_message("Landing on runway 1",air_india)