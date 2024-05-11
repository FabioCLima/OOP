# point.py
"""
A class that represents a 2D point in space.
"""


class Point:
    """
    Represents a point in a 2D coordinate system.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a new instance of the Point class.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft: "Point", upright: "Point") -> bool:
        """
        Checks if the point falls within a rectangle defined by the lower-left
        and upper-right points.

        Args:
            lowleft (Point): The lower-left corner of the rectangle.
            upright (Point): The upper-right corner of the rectangle.

        Returns:
            bool: True if the point falls within the rectangle, False
            otherwise.
        """
        if lowleft.x < self.x < upright.x and lowleft.y < self.y < upright.y:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        Returns a string representation of the Point object.

        Returns:
            str: The string representation of the Point object.
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Point object.

        Returns:
            str: The string representation of the Point object. Can be used to
            recreate the object.
        """
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        """
        Compares the Point object with another object for equality.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __sub__(self, other: "Point") -> "Point":
        """
        Subtracts the coordinates of another Point object from the current
        Point object.

        Args:
            other (Point): The other Point object to subtract.

        Returns:
            Point: A new Point object representing the result of the
            subtraction.
        """
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)
