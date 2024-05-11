# test_car.py
'''
Test module for module Car class only.
'''

import pytest
from source.car.car import Car


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


class TestCar:
    """Test class for the Car parent class in src.car module"""

    def setup_method(self, method):
        """Setup method executed before each test method"""
        print(f"Setting up {method.__name__}")
        self.car = Car('Volvo', 'suv', 2024)
        self.used_car = Car('bmw', 'sedan', 2023)
        self.used_car._odometer_reading = 19

    def teardown_method(self, method):
        """Teardown method executed after each test method"""
        print(f"Tearing down {method.__name__}")
        del self.car
        del self.used_car

    def test_get_descriptive_name(self):
        """Test of the get_descriptive_name method"""
        expected_result = "2024 Volvo Suv"
        result = self.car.get_descriptive_name()
        assert result == expected_result

    def test_odometer_reading_property(self):
        """Test the odometer_reading property"""
        # Set the odometer reading
        self.car.odometer_reading = 100
        # Check if the odometer reading is set correctly
        assert self.car.odometer_reading == 100

        # Try to roll back the odometer
        with pytest.raises(ValueError):
            self.car.odometer_reading = 50

        # Check if the odometer reading remains unchanged
        assert self.car.odometer_reading == 100

    def test_increment_odometer_positive_value(self):
        """Test increment_odometer with positive value."""
        # Given
        miles = 159
        initial_odometer_reading = self.used_car._odometer_reading

        # When
        self.used_car.increment_odometer(miles)

        # Then
        assert self.used_car._odometer_reading == initial_odometer_reading + miles

    def test_increment_odometer_negative_value(self):
        """Test increment_odometer with negative value."""
        # Given
        miles = -10
        initial_odometer_reading = self.used_car.odometer_reading

        # When
        self.used_car.increment_odometer(miles)

        # Then
        assert self.used_car.odometer_reading == initial_odometer_reading
