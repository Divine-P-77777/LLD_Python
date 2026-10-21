from observer import Observer


class TV(Observer):

    def update(self, new_temp: float):
        print(f"TV temperature = {new_temp}")