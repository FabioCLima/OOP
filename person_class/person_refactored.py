from datetime import datetime


class Person:
    """
    A class representing a person.

    Attributes:
    name (str): Name of the person
    age (int): Age of the person
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
        Returns the name attribute of the person object.

        Example:
            >>> john = Person('John', 30)
            >>> john.get_name()
            'John'
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Updates the name attribute of the person object.

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
    doctest.testmod()
