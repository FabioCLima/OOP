# test_restaurant.py
import pytest

# Import Restaurant class
from src.restaurant import Restaurant


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


# Define a test function for the attributes.
def test_attributes_initialize():
    # Given
    # Setup the input values or any preconditions for the test
    arc = Restaurant("Arc", "mediterranea")
    expected_output_name = "Arc"
    expected_output_cuisine_type = "mediterranea"

    # When
    # Call the method will be tested - "__init__"
    result_name = arc.name
    result_cuisine_type = arc.cuisine_type

    # Then
    assert result_name == expected_output_name, "verify the object created"
    assert (
        result_cuisine_type == expected_output_cuisine_type
    ), "verify the object created"


# Definition for the method describe_restaurant
def test_describe_restaurant(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    arc = Restaurant("Arc", "mediterranea")
    expected_restaurant_description = (
        f"The restaurant name is {arc.name}, and its cuisine type is {arc.cuisine_type}")

    # When
    # Call the method you want to test
    arc.describe_restaurant()

    # Then
    # Capture the printed output and check if it matches the expected output
    captured = (
        capsys.readouterr()
    )  # Assuming you are using capsys fixture for capturing stdout
    error_msg = "Verify the describe_restaurant method"
    assert captured.out.strip() == expected_restaurant_description, error_msg


def test_open_restaurant(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    arc = Restaurant("Arc", "mediterranea", is_open=True)
    expected_open_restaurant = f"The {arc.name} restaurant is open"

    # When
    # Call the method you want to test
    arc.open_restaurant()

    # Then
    # Capture the printed output and check if it matches the expected output
    captured = capsys.readouterr()
    error_msg = "Verify the open_restaurant method"
    assert captured.out.strip() == expected_open_restaurant, error_msg
