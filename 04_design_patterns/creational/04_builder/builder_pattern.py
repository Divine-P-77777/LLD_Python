# ==================================
# 1. PRODUCT
# ==================================

class Laptop:

    def __init__(self):
        self.processor = None
        self.ram = None
        self.graphic_card = None
        self.color = None
        self.screen_size = None

    def display_specs(self):
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram}GB")

        if self.graphic_card:
            print(f"Graphic Card: {self.graphic_card}")

        if self.color:
            print(f"Color: {self.color}")

        if self.screen_size:
            print(f"Screen Size: {self.screen_size}")


# ==================================
# 2. BUILDER
# ==================================

class LaptopBuilder:

    def __init__(self):
        self._laptop = Laptop()

    def set_processor(self, processor: str):
        self._laptop.processor = processor
        return self

    def set_ram(self, ram: int):
        self._laptop.ram = ram
        return self

    def set_graphic_card(self, graphic_card: str):
        self._laptop.graphic_card = graphic_card
        return self

    def set_color(self, color: str):
        self._laptop.color = color
        return self

    def set_screen_size(self, screen_size: str):
        self._laptop.screen_size = screen_size
        return self

    def build(self) -> Laptop:

        if not self._laptop.processor or not self._laptop.ram:
            raise ValueError("Processor and RAM are required")

        return self._laptop


# ==================================
# 3. CLIENT
# ==================================

laptop = (
    LaptopBuilder()
    .set_processor("i5-13420H")
    .set_ram(16)
    .set_color("Black")
    .set_screen_size("15.6 inch")
    .set_graphic_card("RTX 4050")
    .build()
)

laptop.display_specs()