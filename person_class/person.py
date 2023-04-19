# person_class/person.py

class Person:
    """
    A class representing a person.

    Attributes:
    __name (str): Name of the person
    __age (int): Age of the person
    """

    def __init__(self, name: str, age: int):
        """
        Constructor for initializing the Person class.

        Args:
        name (str): Name of the person
        age (int): Age of the person
        """
        self.__name = name
        self.__age = age
        
    """
    In the code above we have a class Person, with two attributes, name and age.
    To access theses attributes outside the class, we can use methods also known
    as getter and setter methods.
    
    Getter methods are used to access the value of an attribute and setter methods
    are used to change the value of the attribute.
    """
    
    def get_name(self) -> str:
        """
        Returns the name attribute of the person object.
        """
        return self.__name
    
    def set_name(self, name: str) -> None:
        """
        Updates the name attribute of the person object.
        """
        self.__name = name

    def get_age(self) -> int:
        """
        Returns the age attribute of the person object.
        """
        return self.__age

    def set_age(self, age: int):
        """
        Updates the age attribute of the person object.
        
        """
        self.__age = age
        
    """ 
    The below methods are called special methods. These methods allow us to define how instances
    of our class should be represented as strings.
    """
        
    def __str__(self) -> str:
        """
        Returns a string representation of the person object.
        """
        return f"{self.__name}, {self.__age}"
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the person object
        that can be used to recreate the object.
        """
        return f"Person('{self.__name}', {self.__age})"
