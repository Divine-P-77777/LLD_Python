from transport_mode import TransportMode

class WalkingMode(TransportMode):

    def eta(self):
        print("Walking will take 15 mins")

    def directions(self):
        print("Go straight and take left")