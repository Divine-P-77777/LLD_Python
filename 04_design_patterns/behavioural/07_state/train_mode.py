from transport_mode import TransportMode

class TrainMode(TransportMode):

    def eta(self):
        print("Train will take 5 mins")

    def directions(self):
        print("Just sit in your coach")