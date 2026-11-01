from transport_mode import TransportMode

class TransportService:

    def __init__(self, mode: TransportMode):
        self._mode = mode

    def set_mode(self, new_mode: TransportMode):
        self._mode = new_mode

    def eta(self):
        self._mode.eta()

    def directions(self):
        self._mode.directions()