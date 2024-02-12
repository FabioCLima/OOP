# Class Attribute:

"""   
  class Person:
    
    current_year = 2023

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.born_year = Person.current_year - age
        
    def get_born_year(self):
        return self.born_year
"""

"""
the __str__ method is a special method that is used to define a string representation of 
an object. The __str__ method should return a string that gives a concise and meaningful 
representation of the object.

A class representation of a person with a name and an age.

Properties
current_year: A class-level data representing the current year in which this object is instantiated.
name: A string representing the name of a person.
age: An integer representing the age of a person.
Method
__init__(self, name: str, age: int) -> None: The constructor method of the class. It is used to initialize the 
instance variables name and age of a person.
__str__(self) -> str: Returns a string representation of the Person object in a 
human-readable format.
__repr__(self) -> str: Returns a string representation of the Person object, 
meant for developers and debugging purposes.
get_born_year(self): Returns the year in which a person was born based on 
the current_year and age of the person.
"""
from datetime import datetime

class Person:
    
    current_year = datetime.now().year
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the object.
        Returns:
            str: a human-readable string representation of the object
        """     
        return f"Person(name = {self.name}, age = {self.age})"
    
    def __repr__(self) -> str:
        """
        Method that returns a string representation of the object that can be used to recreate it.
        Returns:
            str: a string representation of the instance.
        """  
        return f"{__class__.__name__}({self.name},{self.age})"
        # return f"{type(self).__name__}({self.name},{self.age})"
        
    def get_born_year(self):
        return Person.current_year - self.age 
    
   
if __name__ == "__main__":
    person1 = Person("John", 30)
    print(person1)
    print(repr(person1))
    person2 = Person("Jane", 25)

    print(person1.get_born_year()) # 1993
    print(person2.get_born_year()) # 1998
    print(person1.__dict__)
    print(vars(person1))
    person = Person("John Doe", 25)
    print(person)
    
    print(repr(person))
    person.get_born_year()


