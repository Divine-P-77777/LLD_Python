from transport_mode import TransportMode

class BikeMode(TransportMode):

    def eta(self):
        print("Bike will take 10 mins")

    def directions(self):
        print("Go to flyover")