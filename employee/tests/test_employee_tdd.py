# test_employee_tdd.py
'''
Using Test-Driven Development approach to the develop the `Employee` class
'''
from src.employee_tdd import Employee


def test_raise_with_default_salary():
    """Test for the give_raise method with default value."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    default_amount = 140000 * 0.1
    expected_salary = 140000 + default_amount  # Expected annual salary after raising by default

    # When
    emp.give_raise()  # Raises annual salary by default amount

    # Then
    assert emp.annual_salary == expected_salary, "Salary not raised by default amount"


def test_raise_with_custom_salary():
    """Test for the give_raise method with custom value.
    """
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    custom_amount = 25000
    expected_salary = 140000 + custom_amount  # Expected annual salary after raising by default

    # When
    emp.give_raise(custom_amount)  # Raises annual salary by default amount

    # Then
    assert emp.annual_salary == expected_salary, "Salary not raised by custom amount"


def test_str_method():
    """Test for the __str__ method."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    expected_str = "Employee: Fabio Lima, Annual Salary: $140000.00"

    # When
    result_str = str(emp)  # Call the __str__() method

    # Then
    assert result_str == expected_str, "__str__ method does not produce the expected string representation"


def test_repr_method():
    """Test for the __repr__ method."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    expected_repr = "Employee('Fabio', 'Lima', 140000.00)"

    # When
    result_repr = repr(emp)  # Call the __repr__() method

    # Then
    assert result_repr == expected_repr, "__repr__ method does not produce the expected string representation"
