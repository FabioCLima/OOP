# test_dog.py
import pytest
# Import Dog class
from src.dog import Dog


@pytest.fixture
def capsys_fixture(capsys):
    return capsys


# Define test functions using pytest conventions
def test_initialize_attributes():
    # Given
    # Setup the input values or any preconditions specific to this t
    duque = Dog("Duque", 5)
    expected_output_name = "Duque"
    expected_output_age = 5

    # When
    # Call the method you want to test
    result_name = duque.name
    result_age = duque.age

    # Then
    assert result_name == expected_output_name, "Verify the name of the dog"
    assert result_age == expected_output_age, "Verify the provided age"


# Defining tests for the created methods on the Dog class sit and roll_over
def test_sit_method(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    duque = Dog("Duque", 5)
    expected_dog_behavior = "Duque is now sitting."

    # When
    # Call the method you want to test
    duque.sit()

    # Then
    # Capture the printed output and check if it matches the expected output
    captured = (
        capsys.readouterr()
    )  # Assuming you are using capsys fixture for capturing stdout
    error_msg = "Verify the sit method behavior"
    assert captured.out.strip() == expected_dog_behavior, error_msg


def test_roll_over_method(capsys):
    # Given
    # Setup the input values or any preconditions specific to this test
    duque = Dog("Duque", 5)
    expected_dog_behavior = "Duque rolled over!"

    # When
    # Call the method you want to test
    duque.roll_over()

    # Then
    # Capture the printed output and check if it matches the expected output
    # Assuming you are using capsys fixture for capturing stdout
    captured = capsys.readouterr()
    error_msg = "Verify the roll_over method behavior"
    assert captured.out.strip() == expected_dog_behavior, error_msg
