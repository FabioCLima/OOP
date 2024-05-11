# shape2.py
'''
Module to represent geometric shapes and calculate their properties.

Classes:
    - Shape: Represents a geometric shape.

        Methods:
            - perimeter(): Calculates the perimeter of the shape. Must be
            overridden by subclasses.
            - area(): Calculates the area of the shape. Must be overridden
            by subclasses.

'''


class Shape():   # parent class

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
