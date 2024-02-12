from dog import Dog

my_dog = Dog('Fred', 5)
your_dog = Dog('Ducky', 6)

print(my_dog)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print("")

print(your_dog)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
print("")
# Calling Instance Methods
print("The instance behaviors....")
my_dog.sit()
my_dog.roll_over()
print("")
your_dog.sit()
your_dog.roll_over()
