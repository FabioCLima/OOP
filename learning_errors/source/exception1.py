# exceptio_1.py
'''
Module to use to review errors in Python.

This module defines two classes: Car and Garage. Car represents a car with make and model attributes.
Garage represents a garage that can hold cars. It has methods to add cars and to get the number of cars in the garage.
'''


class Car:
    """
    Represents a car with make and model attributes.
    """

    def __init__(self, make: str, model: str) -> None:
        """
        Initialize a Car object.

        Parameters:
        - make (str): The make of the car.
        - model (str): The model of the car.
        """
        self.make = make
        self.model = model

    def __repr__(self) -> str:
        """
        Return a string representation of the Car object.
        """
        class_name = self.__class__.__name__
        return f"{class_name}(make={self.make}, model={self.model})"


class Garage:
    """
    Represents a garage that can hold cars.
    """

    def __init__(self) -> None:
        """
        Initialize a Garage object.
        """
        self.cars = []

    def __len__(self) -> int:
        """
        Return the number of cars in the garage.
        """
        return len(self.cars)

    def add_car(self, car: Car):
        """
        Add a Car object to the garage. The main purpose of this method, is to enforce data
        integrity and prevent the addition of objects that don't conform to the expected type.

        Parameters:
        - car (Car): The car object to add to the garage.

        Raises:
        - TypeError: If the input is not a Car object.
        """
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects to the garage.")
        self.cars.append(car)


if __name__ == "__main__":

    fiesta = Car('Ford', 'Fiesta')
    print(fiesta)
    ford = Garage()
    ford.add_car(fiesta)
    print(len(ford))
    # ford.add_car('Ka')
