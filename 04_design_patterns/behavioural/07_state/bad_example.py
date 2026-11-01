from enum import Enum

class TransportMode(Enum):
    WALKING = "walking"
    BIKE = "bike"
    TRAIN = "train"


class TransportService:
    def __init__(self, transport_mode: TransportMode):
        self._transport_mode = transport_mode

    def set_mode(self, new_mode: TransportMode):
        self._transport_mode = new_mode

    def eta(self):
        if self._transport_mode == TransportMode.WALKING:
            print("Walking will take 15 mins")
        elif self._transport_mode == TransportMode.BIKE:
            print("Bike will take 10 mins")
        elif self._transport_mode == TransportMode.TRAIN:
            print("Train will take 5 mins")

    def directions(self):
        if self._transport_mode == TransportMode.WALKING:
            print("Go straight and take left")
        elif self._transport_mode == TransportMode.BIKE:
            print("Go to flyover")
        elif self._transport_mode == TransportMode.TRAIN:
            print("Just sit in your coach")


# Client
service = TransportService(TransportMode.BIKE)
service.eta()
service.directions()



# Problems:
# 1. Long if-else chains: Every transport mode requires additional conditions.
# 2. Tight coupling: TransportService knows the implementation of every transport mode.
# 3. OCP Violation: Adding Airplane or Boat requires modifying existing methods.
# 4. Poor maintainability: Business logic becomes difficult to manage as modes increase.