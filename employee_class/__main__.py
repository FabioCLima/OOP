#OOP/employee_class/__main__.py

from src.employee import Employee


print(f"Show the next employee id: {Employee.get_next_id()}")

# Prompt user for employee name input
employee_name = input("\nPlease enter the employee name: ")

# Validate the name before creating a new instance of Employee class
if Employee.is_valid_name(employee_name):
    # Create a new employee object with valid name
    job_title = input("Type the job title of the new employee. \n")
    employee = Employee(employee_name, job_title)
    print(f"New employee {employee.name} with ID {employee.id} has been created")
    print(employee)
    print(f"The total number of employees created is {Employee.num_employees()}")
    print(f"The current time when this new employee was created is: {Employee.get_current_time()}")
    