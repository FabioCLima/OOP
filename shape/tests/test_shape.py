# test_shape.py
'''
Creating based test class from the Shape class and its subclasses such - Circle

'''

import pytest
from math import pi
import source.shape as shapes


# Test of superclass Circle
class TestCircle:

    """Tests for the Circle(Shape) class"""

    def setup_method(self, method):
        print(f"Setting up {method.__name__}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__}")
        del self.circle

    def test_input_radius(self):
        with pytest.raises(ValueError):
            shapes.Circle(-4)

    def test_perimeter_circle(self):

        expected_perimeter = round(2 * pi * self.circle.radius, 2)
        perimeter = self.circle.perimeter()
        assert round(perimeter, 2) == expected_perimeter

    def test_area_circle(self):
        expected_area = round(pi * self.circle.radius ** 2, 2)
        area = self.circle.area()
        assert round(area, 2) == expected_area
