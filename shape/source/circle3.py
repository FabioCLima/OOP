# circle3.py
"""
Creating read-writes attributes
"""
from shape2 import Shape


class Circle(Shape):
    """
    Represents a circle, a subclass of Shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        __init__(radius: float): Initialize a Circle object with the given
        radius.
        __repr__(): Return a string representation of the Circle object.
        perimeter(): Calculate the perimeter of the circle.
        area(): Calculate the area of the circle.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize a Circle object with the given radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        super().__init__()
        self.radius = radius  # assign the attribute first

        # Then check for be negative
        if self.radius < 0:
            raise ValueError("Cannot accept a negative radius number")

    @property
    def radius(self):
        """
        The radius property.

        Returns:
            float: The radius of the circle.
        """
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """
        Set the radius property.

        Parameters:
            value (float): The value to set as the radius.
        """
        print("Set radius")
        self._radius = float(value)

    @property
    def diameter(self):
        print("Get the radius = self.radius * 2")
        return self.radius * 2

    @diameter.setter
    def diameter(self, value: float):
        self.radius = value / 2
