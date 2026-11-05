class Laptop:
    def __init__(
        self,
        processor: str,
        ram: str,
        graphic_card: str = None,
        color: str = None,
        screen_size: str = None
    ):
        self.processor = processor
        self.ram = ram
        self.graphic_card = graphic_card
        self.color = color
        self.screen_size = screen_size

    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram}")

        if self.graphic_card:
            print(f"Graphic Card: {self.graphic_card}")

        if self.color:
            print(f"Color: {self.color}")

        if self.screen_size:
            print(f"Screen Size: {self.screen_size}")


# Client
laptop = Laptop("i5-13420H", "16GB", None, "Black", "15.6 inch")
laptop.display_specs()


# Problems:
# 1. Long Constructor: Too many parameters make object creation confusing.
# 2. Optional Parameters: Difficult to remember parameter positions.
# 3. Poor Readability: None values make object creation less expressive.
# 4. Less Flexibility: Difficult to construct objects step-by-step.