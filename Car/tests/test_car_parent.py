# test_car_parent.py
'''
Tests related to Car class only.
'''

import pytest
from src.car import Car


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


class TestCarClass:
    """Test class for the Car parent class in src.car module"""

    def setup_method(self, method):
        """Setup method executed before each test method"""
        print(f"Setting up {method.__name__}")
        self.car = Car('Volvo', 'suv', 2024)
        self.used_car = Car('bmw', 'sedan', 2023)
        self.used_car.odometer_reading = 19

    def teardown_method(self, method):
        """Teardown method executed after each test method"""
        print(f"Setting up {method.__name__}")
        del self.car
        del self.used_car

    def test_get_descriptive_name(self):
        """Test of the get_descriptive_name method"""
        expected_result = "2024 Volvo Suv"
        result = self.car.get_descriptive_name()
        assert result == expected_result

    def test_read_odometer(self, capsys):
        """Test of the read_odometer method"""
        expected_result = f"This car has {self.car.odometer_reading} miles on it.\n"
        self.car.read_odometer()
        captured = capsys.readouterr()
        assert captured.out == expected_result

    def test_update_odometer_custom_mileage(self):
        """Test of the update_odometer method"""
        mileage = 100
        expected_result = mileage  # self.car.odometer_reading = 0
        result = self.car.update_odometer(100)
        assert result == expected_result

    def test_update_odometer_bad_mileage(self):
        """Test of the update_odometer method with invalid mileage."""
        # Given - Set initial odometer reading
        self.used_car.odometer_reading = 100

        # When - (Attempt to roll back the odometer)
        mileage = 70
        expected_result = 100  # Expected result is the current odometer reading
        result = self.used_car.update_odometer(mileage)

        # Then - Assert that the result matches the expected result
        assert result == expected_result, "Update should fail for invalid mileage"

    def test_increment_odometer_positive_value(self):
        """Test of increment_odometer with positive value."""
        # Given - Setting the amount of increment_odometer = value > 0
        miles = 159
        expected_result = self.used_car.odometer_reading + miles

        # When
        result = self.used_car.increment_odometer(miles)

        # Then
        assert result == expected_result

    def test_increment_odometer_negative_value(self):
        """Test of increment_odometer with negative value."""
        # Given - Setting the amount of increment_odometer = value > 0
        miles = -10
        expected_result = self.car.odometer_reading + miles

        # When - attempt to use negative value to increment the odometer
        result = self.used_car.increment_odometer(miles)

        # Then
        assert result == expected_result, "increment should fail for invalid miles"
