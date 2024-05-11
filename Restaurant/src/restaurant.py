# restaturant.py


class Restaurant:
    def __init__(self,
                 name: str,
                 cuisine_type: str,
                 is_open: bool = False) -> None:

        self.name = name
        self.cuisine_type = cuisine_type
        self.is_open = is_open

    def describe_restaurant(self) -> None:
        print(
            f"The restaurant name is {self.name}, and its cuisine type is\
 {self.cuisine_type}."
        )

    def open_restaurant(self) -> None:
        if self.is_open:
            print(f"The {self.name} restaurant is open")
