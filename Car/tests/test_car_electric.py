# test_car_eletric.py
'''
Tests related to the superclass ElectricCar(Car)
'''
import pytest
from src.car import ElectricCar


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


class TestElectricCarClass:
    """Test class for the ElectricCar child class in src.car module"""

    def setup_method(self, method):
        """Setup method executed before each test method"""
        print(f"Setting up {method.__name__}")
        self.electric_car = ElectricCar('Tesla', 'Model S', 2022)

    def teardown_method(self, method):
        """Teardown method executed after each test method"""
        print(f"Setting up {method.__name__}")
        del self.electric_car

    def test_describe_battery(self, capsys):
        """Test the describe_battery method of ElectricCar"""
        expected_output = f"This car has a {self.electric_car.battery_size} - kWh battery."
        self.electric_car.describe_battery()  # Call describe_battery method
        captured = capsys.readouterr()  # Capture the output
        assert captured.out.strip() == expected_output.strip()  # Assert that the captured output matches the expected output

    def test_electric_car_repr(self):
        """Test the __repr__ method override of ElectricCar"""
        expected_repr = "ElectricCar(make='Tesla', model='Model S', year=2022, battery_size=40)"
        assert repr(self.electric_car) == expected_repr
