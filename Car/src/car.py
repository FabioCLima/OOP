# car.py
'''
Attempt to model a car ...
& an Eletric car as child class based on Car class
'''


class Car:
    """A simple attempt to represent a car."""

    def __init__(self,
                 make: str,
                 model: str,
                 year: int):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = False

    def __repr__(self):
        """Return a string representation of the car."""
        class_name = self.__class__.__name__
        return f"{class_name}(make='{self.make}', model='{self.model}',\
 year={self.year})"

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage: int) -> int:
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return self.odometer_reading
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int) -> int:
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
            return self.odometer_reading
        else:
            print("You can't increment the odometer with negative value.")

    def fill_gas_tank(self):
        """Fill the gas tank of the car if it's empty."""
        if not self.gas_tank:
            print("Filling gas tank...")
            self.gas_tank = True
        else:
            print("Gas tank is already full.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # composition
