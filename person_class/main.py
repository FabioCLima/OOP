from person import Person

# Creating a Person object
person = Person("John Doe", 25)

# Priting the person instance created
print(f"Printing the person object created: {person}")

# print the object using __repr__
print(f"String representation of the object can be use to recreate it {repr(person)}") 

# Getting the person's name
print("Getting the person's name object")
print(person.get_name())

# Changing the person's name
print("Changing the person's name")
person.set_name("Jane Doe")

# Getting the person's age
print("Getting the person's age")
print(person.get_age())

# Changing the person's age
print("Changing the person's age")
person.set_age(30)

# Getting the updated details
print(person.get_name())
print(person.get_age())
