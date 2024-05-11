# test_car.py
import pytest
from src.car import Car


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


def test_initialize_attributes(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    make = "Toyota"
    model = "Camry"
    year = 2022

    # When
    # Create a car instance
    car = Car(make, model, year)

    # Then
    # Access the attributes and verify their values
    result_make = car.make
    result_model = car.model
    result_year = car.year
    result_odometer_reading = car.odometer_reading

    # Assert the results against the expected values
    assert result_make == make, "Verify the make attribute"
    assert result_model == model, "Verify the model attribute"
    assert result_year == year, "Verify the year attribute"
    error_msg_odometer_reading = "Verify the odometer_reading attribute is \
    initialized to 0"
    assert result_odometer_reading == 0, error_msg_odometer_reading


# Define test function for the get_descriptive_name method
def test_get_descriptive_name(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    make = "Toyota"
    model = "Camry"
    year = 2022

    # Create a car instance
    car = Car(make, model, year)

    # When
    # Call the get_descriptive_name method
    descriptive_name = car.get_descriptive_name()

    # Then
    # Capture the printed output and check if it matches the expected output
    expected_output = f"{year} {make} {model}".title()
    error_msg = "Verify the get_descriptive_name method"
    assert descriptive_name == expected_output, error_msg


# Define test function for the read_odometer method
def test_read_odometer(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    make = "Toyota"
    model = "Camry"
    year = 2022
    # Assuming the odometer reading is set to 50000 miles
    odometer_reading = 50000

    # Create a car instance
    car = Car(make, model, year)
    # Set the odometer reading for the car instance
    car.odometer_reading = odometer_reading

    # When
    # Call the read_odometer method
    car.read_odometer()

    # Then
    # Capture the printed output and check if it matches the expected output
    expected_output = f"This car has {odometer_reading} miles on it."
    # Assuming you are using capsys fixture for capturing stdout
    captured = capsys.readouterr()
    error_msg = "Verify the read_odometer method"
    assert captured.out.strip() == expected_output, error_msg


# Define test function for the update_odometer method
def test_update_odometer():
    # Given
    # Setup the input values or any preconditions specific to this test
    make = "Toyota"
    model = "Camry"
    year = 2022
    initial_odometer_reading = 50000  # Initial odometer reading
    new_odometer_reading = 60000  # New odometer reading

    # Create a car instance
    car = Car(make, model, year)
    car.odometer_reading = initial_odometer_reading  # Set the initial odometer reading

    # When
    # Call the update_odometer method with a valid mileage
    car.update_odometer(new_odometer_reading)

    # Then
    # Check if the odometer reading has been updated correctly
    assert car.odometer_reading == new_odometer_reading, "Verify odometer update"


# Define test function for the increment_odometer method
def test_increment_odometer():
    # Given
    # Setup the input values or any preconditions specific to this test
    make = "Toyota"
    model = "Camry"
    year = 2022
    initial_odometer_reading = 50000  # Initial odometer reading
    increment_value = 100  # Increment value

    # Create a car instance
    car = Car(make, model, year)
    car.odometer_reading = initial_odometer_reading  # Set the initial odometer reading

    # When
    # Call the increment_odometer method with a positive increment value
    car.increment_odometer(increment_value)

    # Then
    # Check if the odometer reading has been incremented correctly
    expected_odometer_reading = initial_odometer_reading + increment_value
    assert car.odometer_reading == expected_odometer_reading, "Verify odometer increment"
