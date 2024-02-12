# Classes/python projects

class Dog:
    """
    A simple attempt to model a dog.
    """    
    def __init__(self, name: str, age: int) -> None:
        """
        Initialize name and age attributes.

        Args:
            name (str): The name of the dog.
            age (int): The age of the dog.
        """
        self.name = name
        self.age = age 
        
    def __str__(self) -> str:
        """
        String representation of the dog.

        Returns:
            str: A string that represents the dog
        """ 
        return f"Dog(name={self.name}, age={self.age})"
               
    
    # behaviors    
    def sit(self):
        """
        Simulate a dog sitting in response to a command
        """                 
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """
        Simulate rolling over in response to a command
        """
        print(f"{self.name} rolled over!")        
        