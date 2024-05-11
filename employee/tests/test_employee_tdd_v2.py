# test_employee_tdd_v2.py
'''
Use descriptive test names: While your test names are informative,
you could make them more descriptive by explicitly mentioning the
behavior being tested. For example, instead of
test_raise_default_salary(), you could name it
test_raise_salary_with_default_amount().
'''
import pytest
from src.employee_tdd import Employee


@pytest.mark.parametrize("raise_amount, expected_salary", [
    (None, 154000),  # Default raise amount
    (25000, 165000)  # Custom raise amount
])
def test_raise_salary(raise_amount, expected_salary):
    """Test the give_raise method with different raise amounts."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)

    # When
    emp.give_raise(raise_amount)

    # Then
    assert emp.annual_salary == expected_salary, f"Salary not raised by {raise_amount} amount"


def test_str_method():
    """Test the __str__ method."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    expected_str = "Employee: Fabio Lima, Annual Salary: $140000.00"

    # When
    result_str = str(emp)

    # Then
    assert result_str == expected_str


def test_repr_method():
    """Test the __repr__ method."""
    # Given
    emp = Employee("Fabio", "Lima", 140000)
    expected_repr = "Employee('Fabio', 'Lima', 140000.00)"

    # When
    result_repr = repr(emp)

    # Then
    assert result_repr == expected_repr
