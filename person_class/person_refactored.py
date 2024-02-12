from datetime import datetime

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

        Example:
            >>> john = Person('John', 30)
            >>> print(john.get_name())
            'John'
            >>> print(john.get_age())
            30
        """
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """
        Returns the name attribute of the person object.This a getter method.

        Example:
            >>> john = Person('John', 30)
            >>> john.get_name()
            'John'
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Updates the name attribute of the person object. This is a setter method.

        Example:
            >>> john = Person('John', 30)
            >>> john.set_name('Johnny')
            >>> john.get_name()
            'Johnny'
        """
        self._name = name

    @property
    def age(self) -> int:
        """
        Returns the age attribute of the person object.

        Example:
            >>> john = Person('John', 30)
            >>> john.get_age()
            30
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """
        Updates the age attribute of the person object.

        Example:
            >>> john = Person('John', 30)
            >>> john.set_age(35)
            >>> john.get_age()
            35
        """
        if not isinstance(age, int):
            raise ValueError("Age must be a integer")
        
        elif age < 0:
            raise ValueError("Age must be a positive integer.")
        else:
            self._age = age

    def year_of_birth(self) -> int:
        """
        Returns the year of birth of the person object.

        Example:
            >>> john = Person('John', 30)
            >>> john.year_of_birth()
            1991
        """
        current_year = datetime.now().year
        return current_year - self._age

    def __str__(self) -> str:
        """
        Returns a string representation of the person object.

        Example:
            >>> john = Person('John', 30)
            >>> str(john)
            'John, 30'
        """
        return f"{self._name}, {self._age}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the person object
        that can be used to recreate the object.

        Example:
            >>> john = Person('John', 30)
            >>> repr(john)
            "Person('John', 30)"
        """
        return f"Person('{self._name}', {self._age})"


import doctest

if __name__ == "__main__":
    # doctest.testmod()
    
    p1 = Person("Leonildo", 93)
    p2 = Person("Tim", 29)
    p3 = Person("Nobody", 0)
    p4 = Person("Jose", 'forty')

print(f"The age of person1 is {p1.age} years old.")
p1.age = 95
print(f"The new age of person1 is {p1.age} years old.")
print()
print(f"The age of nobody is {p3.age} years old.")
p3.age = -5
