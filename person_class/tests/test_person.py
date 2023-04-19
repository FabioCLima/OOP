from person_class.person import Person

def test_person_creation():
    """
    Test creating an instance of the Person class
    """
    person = Person("John", 30)
    assert person.name == "John"
    assert person.age == 30
