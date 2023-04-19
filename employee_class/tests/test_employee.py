import pytest
import sys
import os.path

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.path.pardir))
sys.path.append(parent_dir)

from src.employee import Employee

def test_employee():
    # Test creating an employee with valid name
    emp1 = Employee('John Doe', 'Software Developer')
    assert emp1.name == 'John Doe'
    assert emp1.job_title == 'Software Developer'
    assert emp1.id == 1

    # Test creating an employee with another valid name
    emp2 = Employee('Jane Smith', 'Sales Associate')
    assert emp2.name == 'Jane Smith'
    assert emp2.job_title == 'Sales Associate'
    assert emp2.id == 2

    # # Test creating an employee with an invalid name (None)
    # with pytest.raises(TypeError):
    #     emp3 = Employee(None, 'Manager')

    # # Test creating an employee with an empty name
    # with pytest.raises(ValueError):
    #     emp4 = Employee('', 'Engineer')

    # Test getting the next available ID
    assert Employee.get_next_id() == 3

    # Test incrementing the number of employees
    assert emp2.increment_num_employees() == 2
