# class definition for training getter and setter methods
# article 1
from datetime import date


class Cat:
    
    """ A simple class to model a cat object."""    

    def __init__(self, name: str, dob: date) -> None:
        """Constructor method of the Cat class.

        Args:
            name (str): The name of the cat.
            dob (date): The date of birth of the cat.
        """
        self.name = name
        self.dob = dob

    def __str__(self) -> str:
        """Returns a string representation of the Cat object."""
        return f"Cat(name={self.name}, date of birth={self.dob})"
    
    """
    The '@property' is a way to access and assign the value of an instance variable of a class
    through a method. The method associated with the variable using a decorator is called the 
    getter (@property), while the method associated with the variable using a setter decorator
    '@<variable>.setter is called setter. These methods allow safe and convenient read and write
    access to the instance variables.
    
    The getter method needs to be defined before the setter method can use it to get the value 
    the instance variable
    """
    @property
    def name(self) -> str:
        """Getter method that returns the name of the cat as a string."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Setter method that sets the name of the cat.

        Args:
            name (str): The new name of the cat.

        Raises:
            ValueError: If the name is not alphanumeric.
        """
        if not name.isalnum():
            raise ValueError('Sorry, name needs to be alphanumeric')
        self._name = name

    @property
    def dob(self) -> date:
        """Getter method that returns the date of birth of the cat as a date object."""
        return self._dob

    @dob.setter
    def dob(self, dob: date) -> None:
        """Setter method that sets the date of birth of the cat.

        Args:
            dob (date): The new date of birth of the cat.
        """
        self._dob = dob

    @property
    def age(self) -> int:
        """Getter method that calculates and returns the age of the cat."""
        today = date.today()
        age = today.year - self.dob.year
        if today.month < self.dob.month or (today.month == self.dob.month and today.day < self.dob.day):
            age -= 1
        return age
