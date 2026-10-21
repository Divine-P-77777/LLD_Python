from observer import Observer


class PhoneDisplay(Observer):

    def update(self, new_temp: float):
        print(f"Phone display temperature = {new_temp}")