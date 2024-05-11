# shape.py
'''
Module to represent geometric shapes and calculate their properties.

Classes:
    - Shape: Represents a geometric shape.

        Methods:
            - perimeter(): Calculates the perimeter of the shape. Must be overridden by subclasses.
            - area(): Calculates the area of the shape. Must be overridden by subclasses.

    - Circle: Represents a circle, a subclass of Shape.

        Methods:
            - perimeter(): Calculates the perimeter of the circle (overrides Shape's perimeter method).
            - area(): Calculates the area of the circle (overrides Shape's area method).

Relationships:
    The Circle class inherits from the Shape class, signifying that a circle is a specific type of shape
    and shares common properties and behaviors with other shapes. Each subclass defines its own behavior
    for calculating perimeter and area.

'''
from math import pi


# Parent class
class Shape():
    """
    Represents a geometric shape.

    Methods:
        perimeter(): Calculate the perimeter of the shape.
        area(): Calculate the area of the shape.
    """

    def perimeter(self) -> float:
        """
        Abstract method to calculate the perimeter of the shape.
        """
        pass

    def area(self) -> float:
        """
        Abstract method to calculate the area of the shape.
        """
        pass


# Child class  or superclass
class Circle(Shape):
    """
    Represents a circle, a subclass of Shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        __init__(radius: float): Initialize a Circle object with the given radius.
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
            raise ValueError("Input radius should be a non-negative number.")
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return a string representation of the Circle object.
        """
        return f"{self.__class__.__name__}(radius={self.radius})"

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        perimeter = 2 * pi * self.radius
        return round(perimeter, 2)

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        area = pi * self.radius ** 2
        return round(area, 2)
