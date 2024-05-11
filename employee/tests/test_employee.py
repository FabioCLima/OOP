import pytest
from src.employee import Employee


@pytest.fixture
def new_employee():
    """
    Fixture to create an instance of Employee.
    """
    employee = Employee("Fabio", "Lima", 150000)
    return employee


def test_initialize_attributes(new_employee):
    """
    Testing the initializing the attributes of Employee
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    # The fixture 'language_survey' is already providing us with an
    # initialized instance

    # When
    # Since this test is only concerned with verifing the initialization
    # of attributes, there's no specific action needed.

    # Then
    assert new_employee.first_name == "Fabio"
    assert new_employee.last_name == "Lima"
    assert new_employee.annual_salary == 150000


def test_give_default_raise(new_employee):
    """
    This test is checking the default raise value in annual salary. The
    assertion should compare the return value of the give_raise() method
    with the expected value.
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    # The fixture 'new_employee' is already providing us with an
    # initialized instance

    # When
    # Apply the default raise salary value
    result_custom_raise_salary = new_employee.give_raise()

    # Then
    assert result_custom_raise_salary == 155000


def test_give_custom_raise(new_employee):
    """
    This test is checking the custom raise value in annual salary in the
    give_raise method. 
    """
    # Given
    # Setup the an instance of the class with any input values or any
    # preconditions specific to this test
    # The fixture 'new_employee' is already providing us with an
    # initialized instance
    custom_raise_salary = 10000

    # When
    # Apply a custom raise salary value
    result_custom_raise_salary = new_employee.give_raise(custom_raise_salary)

    # Then
    assert result_custom_raise_salary == 160000
