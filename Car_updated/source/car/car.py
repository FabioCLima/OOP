# car.py
'''
Attempt to model a car ...

classes define objects, which contain attributes and related behaviors
(methods).

Python classes provide a reliable way of organizing data. Properties
make it possible to write getters and setters that look the same
as accessing an ordinary attribute.

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
        self._odometer_reading = 0
        self.gas_tank = False

    def __repr__(self) -> str:
        """Return the canonical string representation of the Car
    object"""
        class_name = self.__class__.__name__
        return f"{class_name}(make='{self.make}', model='{self.model}',\
 year={self.year})"

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    @property
    def odometer_reading(self) -> int:
        """Get the car's mileage."""
        return self._odometer_reading

    @odometer_reading.setter
    def odometer_reading(self, mileage: int):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    @odometer_reading.setter
    def odometer_reading(self, mileage: int):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            raise ValueError("Odometer reading cannot be rolled back.")

    def increment_odometer(self, miles: int) -> None:
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            raise ValueError("Increment value must be positive.")


if __name__ == "__main__":
    # Creating a Car object
    nivus = Car('Wolkswagen', 'suv nivus', 2024)
    nivus.gas_tank = True

    # Display the descriptive name of the car
    print(nivus.get_descriptive_name())

    # Check the current odometer reading
    print(f"Odometer reading from my new car - {nivus} is \
{nivus.odometer_reading} km")

    # Set the odometer reading
    try:
        nivus.odometer_reading = 100
    except ValueError as error:
        print(error)

    # Increment the odometer reading
    try:
        nivus.increment_odometer(50)
    except ValueError as error:
        print(error)

    # Fill the gas tank
    nivus.fill_gas_tank()
