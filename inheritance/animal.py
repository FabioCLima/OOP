# animal.py
'''
Inheritance - is a relationship
The derived object can be use to replace the super class objects in the application.
Liskov substitution principle - if S is a subtype of T, then replacing objects of T,
then replacing objects of type T with objects of type S doesn't change the program's
behavior.
'''


class Animal:
    pass


class Horse(Animal):
    '''
    Horse class inherits the interface and implementation of Animal class.
    '''
    pass


animal = Animal()
print(dir(animal))
