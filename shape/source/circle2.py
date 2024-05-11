"""
circle2.py - Module for representing circles and calculating their properties.

    - Circle: Represents a circle, a subclass of Shape.

        Methods:
            - perimeter(): Calculates the perimeter of the circle
            (overrides Shape's perimeter method).
            - area(): Calculates the area of the circle
            (overrides Shape's area method).

    Relationships:
        The Circle class inherits from the Shape class, signifying that a
        circle is a specific type of Shape and shares common properties and
        behaviors with other shapes. Each subclass defines its own behavior
        for calculating perimeter and area.
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
        self._radius = radius  # assign the attribute first

        # Then check for be negative
        if self._radius < 0:
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
        self._radius = value

    @radius.deleter
    def radius(self):
        """Delete the radius property."""
        print("Delete radius")
        del self._radius
