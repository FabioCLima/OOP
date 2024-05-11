"""
A main entry point for an application that performs a few geometry tasks.
"""
from point import Point


def main():
    print("Instantiate a new point object, called point1")
    x = float(input("Type the x-coordinate of point1: "))
    y = float(input("Type the y-coordinate of point1: "))

    point1 = Point(x, y)
    print("The point1 created is:", repr(point1))

    print("Inform the coordinates of the lower-left corner of the rectangle")
    lowleft_x = float(
        input("Type the x-coordinate of the lower-left corner: ")
    )
    lowleft_y = float(
        input("Type the y-coordinate of the lower-left corner: ")
    )

    lowleft_rectangle = Point(lowleft_x, lowleft_y)
    print(
        "The coordinates of the lower-left corner of the rectangle are:",
        repr(lowleft_rectangle),
    )

    print("Inform the coordinates of the upper-right corner of the rectangle")
    upright_x = float(
        input("Type the x-coordinate of the upper-right corner: ")
    )
    upright_y = float(
        input("Type the y-coordinate of the upper-right corner: ")
    )

    upright_rectangle = Point(upright_x, upright_y)
    print(
        "The coordinates of the upper-right corner of the rectangle are:",
        repr(upright_rectangle),
    )

    print("Check if point1 is inside the rectangle")
    is_falling = point1.falls_in_rectangle(
        lowleft_rectangle, upright_rectangle
    )
    print("Does point1 fall inside the rectangle?", is_falling)


if __name__ == "__main__":
    main()
