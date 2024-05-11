# point.py


class Point:

    def __init__(self, x, y) -> None:
        """Initialize two non-public attributes,
        to hold the Cartesian coordinates of point
        at hand.

        Args:
            x (int): _description_
            y (int): _description_
        """
        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x

    def set_x(self, value) -> None:
        self._x = value

    def get_y(self) -> int:
        return self._y

    def set_y(self, value) -> None:
        self._y = value


if __name__ == "__main__":
    p1 = Point(12, 5)
    print(p1._x)
    print(p1.get_y())
    print(p1.set_x(42))
    print(p1.get_x())
    print(p1._x)
    print(p1._y)
