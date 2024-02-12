from cat import Cat
from datetime import date

cat1 = Cat('Pacha', date(2018, 10, 10))
print(cat1)

print(f"The name of the cat is {cat1.name}")

# print("Can change the Pacha's name of instance pacha by doing")
# pacha._name = 'newPacha'

# print(pacha)
# Access the attribute name in no pythonic way - directly
# pacha.set_name('newPacha')
# print(pacha)

print("Access the attributes using the pythonic way, '@property - getter method'")
print("'@<attribute>.setter'")

print("To get or set the new name of the cat1, use the name property:")
cat1.name = "Pachá"
print(f"Pacha's correct name is {cat1.name}")
print()
print("To get or set the date of the birth of the cat, use the dob property:")
cat1.dob = date(2019, 10, 10)
print(f"The birthday of the {cat1.name} is {cat1.dob}")
print()
print(f"To get the age of the {cat1.name}, use the age property:")
print(f"The age of {cat1.name} is {cat1.age}")
