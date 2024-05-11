# point3.py
""" We need an immutable Point class that doesn't allow the user to
mutate the original value of its coordinates, x and y
To achieve this goal. - read only attributes.

"""


class WriteCoordinateError(Exception):
    pass


class Point:
    """
    Represents a point in 2D space.

    Attributes:
        _x (float): The x-coordinate of the point.
        _y (float): The y-coordinate of the point.

    Methods:
        __init__(x: float, y: float): Initialize a Point object with the given
        coordinates.
        x(): Get the x-coordinate of the point.
        y(): Get the y-coordinate of the point.
    """

    def __init__(self, x: float, y: float):
        """
        Initialize a Point object with the given coordinates.

        Parameters:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        """
        Get the x-coordinate of the point.

        Returns:
            float: The x-coordinate of the point.
        """
        return self._x

    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self) -> float:
        """
        Get the y-coordinate of the point.

        Returns:
            float: The y-coordinate of the point.
        """
        return self._y

    @y.setter
    def x(self, value):
        raise WriteCoordinateError("y coordinate is read-only")
