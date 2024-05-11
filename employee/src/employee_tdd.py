# employee_tdd.py
'''A class to model an Employee object'''


class Employee:

    def __init__(
                self,
                first_name: str,
                last_name: str,
                annual_salary: float
                ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.amount = self.annual_salary * 0.1

    def give_raise(
        self,
        raise_amount: float = None
    ) -> float:
        if raise_amount is not None:
            self.annual_salary += raise_amount
        else:
            self.annual_salary += self.amount
        return self.annual_salary

    def __repr__(self) -> str:
        """Return a string representation of the Employee object for
        debugging."""
        return (
            f"{self.__class__.__name__}('{self.first_name}', "
            f"'{self.last_name}', {self.annual_salary:.2f})"
        )

    def __str__(self) -> str:
        """Return a string representation of the Employee object."""
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"Annual Salary: ${self.annual_salary:.2f}"
        )
