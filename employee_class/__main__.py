#OOP/employee_class/__main__.py

from src.employee import Employee


print(f"Show the next employee id: {Employee.get_next_id()}")

# Prompt user for employee name input
employee_name = input("\nPlease enter the employee name: ")

# Validate the name before creating a new instance of Employee class
if Employee.is_valid_name(employee_name):
    # Create a new employee object with valid name
    job_title = 'Data Analyst'
    employee1 = Employee(employee_name, job_title)
    print(f"New employee {employee1.name} with ID {employee1.id} has been created")
    print