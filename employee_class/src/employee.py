# OOP/employee_class/src/employee.py
# author: Fabio Lima
# employee version 1
'''
#! Summary of the ideas study on this class: class method 
-> Class methods can modify the class state, but not the instance state

-> Static methods can't modify either the class state or the instance state and are purely functional.
'''

class Employee:
    """
    A class the models a Employee blueprint with 3 attributes: name, job title and unique id.
    Whenever a new Employee object is created, it will have an ID of class level variable.
    
    Attributes:
    ----------
        name (str): The employee name
        job title (str): The employee job title
        id (int): The employee id
        id_counter (int): A class level variable id_counter which is initialized to 1 
        
    Examples:
    --------
        >>> employee_1 = Employee('John Doe', 'Software Developer')
        >>> employee_1.name
        'John Doe'
        >>> employee_1.job_title
        'Software Developer'
        >>> employee_1.id
        1  
        
    """    
    id_counter: int = 1 
    
    def __init__(self, name, job_title) -> None:
        """
        Initializes three instance variables name, job_title and id. 

        Args:
            name (str): The name of the employee
            job_title (str): The job title of the employee
            id (int): The id variable is incremented using id_counter which is then incremented by 1.
            
        """        
        
        self.name: str = name
        self.job_title: str = job_title
        self.id: id = Employee.id_counter
        # The id_counter class attribute is incremented by 1, which generates a unique id for the employee
        Employee.id_counter += 1
        
    
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the object.
        Returns:
            str: a human-readable string representation of the object
        """
        return f"Employee: name={self.name}, job title={self.job_title}"
    

    @classmethod
    def get_next_id(cls):
        """
        This method allows the user of the class to retrieve the next available ID without
        having to create a new Employee object.
        Returns:
            int: The next id counter which will be related to the next employee object.
        """        
        return cls.id_counter
    
    @classmethod
    def increment_num_employees(cls) -> int:
        """
        This method returns the number of employees created

        Returns:
            int: The number of employee instances created so far.
        """        
        
        return cls.id_counter - 1
    
    @staticmethod
    def is_valid_name(name: str) -> bool:
        """
        This method returns True if the name provided is valid, false otherwise
        Args:
            name (str): The name of the employee

        Returns:
            bool: True if the name provided is valid, False otherwise
        """ 
        return isinstance(name, str) and bool(name.strip())   
    

if __name__ == "__main__":
    
    print(f"Show the next employee id: {Employee.get_next_id()}")
    # Prompt user for employee name input
    employee_name = input("\nPlease enter the employee name: ")
    
    #! Validate the name before creating a new instance of Employee class
    if Employee.is_valid_name(employee_name):
        #! Create a new employee object with valid name
        job_title = 'Data Analyst'
        employee1 = Employee(employee_name, job_title)
        print(f"New employee {employee1.name} with ID {employee1.id} has been created")
        print(f"How many employees were created so far: {employee1.increment_num_employees()}")
    else:
        #! Handle invalid employee name input
        print("Invalid employee name provided. Please enter a valid name.")
    
    print("")
    
    #! Validate the name before creating a new instance of Employee class
    employee_name2 = 'Mario Barbosa'
    if Employee.is_valid_name(employee_name2):
        #! Create a new employee object with valid name
        job_title2 = 'Sales Manager'
        employee2 = Employee(employee_name2, job_title2)
        print(f"New employee {employee2.name} with ID {employee2.id} has been created")
        print(f"How many employees were created so far: {employee2.increment_num_employees()}")
    else:
        #! Handle invalid employee name input
        print("Invalid employee name provided. Please enter a valid name.")
    