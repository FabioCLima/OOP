from src.person_class import Person

p1 = Person('Fabio Lima', 47)
print(p1)

print(f"The age of {p1.name} is {p1.age}")
current_year: int = int(Person.current_year)
print(f"The {p1.name} was born in {current_year - p1.age}")
