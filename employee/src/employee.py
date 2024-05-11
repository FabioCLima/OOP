# employee.py
'''
A class to model a Employee object, the __init__() method should take in a
first name, a last name, and an annual salary, and store each of these as
attribute. Write a method called give_raise() that adds $5000 to annual
salary by default but also accepts a different raise amount.
'''


class Employee:

    """A class to model an Employee object.

    Args:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        annual_salary (float): The annual salary of the employee.

    Examples:
        # Create an employee named John Doe with an annual salary of $50,000
        >>> employee1 = Employee("John", "Doe", 50000.0)

        # Create another employee named Alice Smith with an annual salary of
        # $60,000
        >>> employee2 = Employee("Alice", "Smith", 60000.0)
    """

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 annual_salary: float
                 ) -> None:

        """Initialize an Employee object with provided attributes.

        Args:
            first_name (str): The first name of the employee.
            last_name (str): The last name of the employee.
            annual_salary (float): The annual salary of the employee.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,
                   raise_salary: float = 5000
                   ) -> float:

        """Give a raise to the employee's annual salary.

        Args:
            raise_salary (float, optional): The amount to increase the annual salary by.
                Defaults to 5000.

        Returns:
            float: The updated annual salary after the raise.

        Examples:
            # Give a default raise of $5000 to an employee's annual salary
            >>> employee1.give_raise()
            55000.0

            # Give a raise of $10000 to an employee's annual salary
            >>> employee2.give_raise(10000)
            70000.0
        """
        self.annual_salary += raise_salary
        return self.annual_salary
