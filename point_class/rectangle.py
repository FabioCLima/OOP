"""
A module that defines the Rectangle class for representing rectangles in a 2D
coordinate system.

Classes:
    Rectangle: Represents a rectangle defined by its lower-left and
    upper-right corners.
"""
from point import Point


class Rectangle:
    """
    Represents a rectangle in a 2D coordinate system.

    Attributes:
        lowleft (Point): The lower-left corner of the rectangle.
        upright (Point): The upper-right corner of the rectangle.
    """

    def __init__(self, lowleft: Point, upright: Point) -> None:
        """
        Initializes a new instance of the Rectangle class.

        Args:
            lowleft (Point): The lower-left corner of the rectangle.
            upright (Point): The upper-right corner of the rectangle.
        """
        self.lowleft = lowleft
        self.upright = upright

    def __str__(self) -> str:
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: The string representation of the Rectangle object.
        """
        return f"Rectangle(lowleft={self.lowleft}, upright={self.upright})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: The string representation of the Rectangle object. Can be
            used to recreate the object.
        """
        return f"Rectangle(lowleft={repr(self.lowleft)}, \
                 upright={repr(self.upright)})"


if __name__ == "__main__":
    rectangle1 = Rectangle(Point(5, 4), Point(6, 9))
    print(rectangle1)
