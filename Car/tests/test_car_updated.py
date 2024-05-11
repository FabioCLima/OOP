# test_car_updated.py

'''
Test of Car class and superclass EletricCar

'''
import pytest
from src.car import Car, ElectricCar


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


class TestCar:
    """Test class for the Car class in src.car module
    """

    def setup_method(self, method):
        """Setup method executed before each test method
        """
        print(f"Setting up {method.__name__}")
        self.car = Car('Volvo', 'suv', 2024)
        self.used_car = Car('bmw', 'sedan', 2023)
        self.used_car.odometer_reading = 19
        self.electric_car = ElectricCar('Tesla', 'Model S', 2022)

    def teardown_method(self, method):
        """Teardown method executed after each test method
        """
        print(f"Setting up {method.__name__}")
        del self.car
        del self.used_car
        del self.electric_car

    def test_get_descriptive_name(self):
        """Test of the get_descriptive_name method
        """
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
        """
        Test of the update_odometer method with invalid mileage.
        The method should reject the update and return the current odometer
        reading.
        """
        # Given - Set initial odometer reading
        self.used_car.odometer_reading = 100

        # When - (Attempt to roll back the odometer)
        mileage = 70
        expected_result = 100  # Expected result is the current odometer reading
        result = self.used_car.update_odometer(mileage)

        # Then - Assert that the result matches the expected result
        assert result == expected_result, "Update should fail for invalid mileage"

    def test_increment_odometer_positive_value(self):
        """Test of increment_odometer with positive value.
        """
        # Given - Setting the amount of increment_odometer = value > 0
        miles = 159
        expected_result = self.used_car.odometer_reading + miles

        # When
        result = self.used_car.increment_odometer(miles)

        # Then
        assert result == expected_result

    def test_increment_odometer_negative_value(self):
        """Test of increment_odometer with negative value.
        The method should reject the incrementation negative value and return
        the current odometer reading.
        """
        # Given - Setting the amount of increment_odometer = value > 0
        miles = -10
        expected_result = self.car.odometer_reading + miles

        # When - attempt to use negative value to increment the odometer
        result = self.used_car.increment_odometer(miles)

        # Then
        assert result == expected_result, "incremente should fail for invalid miles"

    # New test method for ElectricCar class
    def test_describe_battery(self, capsys):
        """Test the describe_battery method of ElectricCar"""
        expected_output = f"This car has a {self.electric_car.battery_size} - kWh battery."
        self.electric_car.describe_battery()  # Call describe_battery method
        captured = capsys.readouterr()  # Capture the output
        assert captured.out.strip() == expected_output.strip()  # Assert that the captured output matches the expected output

    # New test method for ElectricCar class
    def test_electric_car_repr(self):
        """Test the __repr__ method override of ElectricCar"""
        expected_repr = "ElectricCar(make='Tesla', model='Model S', year=2022, battery_size=40)"
        assert repr(self.electric_car) == expected_repr