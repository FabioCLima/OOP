# person_class/person.py

# ! Definition of getter and setter methods
""" 
In OOP, getter and setter methods are used to control access to the object's attributes
they allow you to enforce constrains on how the attributes are accessed or  modified, 
which can help to prevent bugs and ensure data consistency.

Getter methods are used to retrieve the current value on attribute.
"""

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
    In the current code these attributes are private, but there in no strict rule for that.
    To access theses attributes outside the class, we can use methods also known
    as getter and setter methods.
    
    Getter methods are used to access the value of an attribute and setter methods
    are used to change the value of the attribute.
    
    Getter and setter methods should be used when you want to control the access
    to the attributes of an object.
    
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
    
    
if __name__ == "__main__":
    
    p1 = Person("Fabio", 46)
    p2 = Person("Raquel", 40)
    
    print("To access these attributes, such as name and age, you can use getter methods")
    name1 = p1.get_name()
    print(f"First person's name: {name1}")
    age1 = p1.get_age()
    print(f"First person's age: {age1}")
    print()
    print("To update the p2 age, you must use the setter method.")
    print("First checking the current value of attribute age from person2:p2 object")
    print(f"The person2'age is {p2.get_age()} years old.")
    p2.set_age(41)
    print(f"The age of person 2 ('p2') object now, is {p2.get_age()}") 
