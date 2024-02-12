from car import Car
from datetime import date

my_new_car = Car('audi', 'a4', date(2024, 1, 1).year)
print(f"The new car object: {my_new_car}")
print("")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modify Attributes Values
# 1 - Modifying an Attribute's Value Directly
print("The simplest way to modify the value of an attribute is to access the attribute directly through an instance")
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modify an Attribute's Value Through a Method
print("It can be helpful to have methods that update certain attributes for you.")
print("Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally")
print()
print('Updating the odometer of mileage = 25')
my_new_car.update_odometer(25)
my_new_car.read_odometer()
print()
print("Updating the car of odometer of mileage = 25 (trying to roll back the odometer)")
my_new_car.update_odometer(15)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', date(2019, 1, 1).year)
print(f"My used car object: {my_used_car}")
print(my_used_car.get_descriptive_name())

# update the used car odometer
my_used_car.update_odometer(23.500)
my_used_car.read_odometer()
print()
my_used_car.increment_odometer(0.100)
my_used_car.read_odometer()
print()
my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

# Create a new car object
car = Car("Honda", "Sedan", date(2021, 1, 1))

# Print the initial speed of the car
print(car.speed)  # Output: 0

# Accelerate the car to 50 km/h
car.accelerate(50)

# Check the current speed of the car after accelerating it
print(car.speed)  # Output: 50

# Brake the car to slow down the speed by 20 km/h
car.brake(20)

# Check the current speed of the car after braking it
print(car.speed)  # Output: 30

# Try to set the speed to a negative value, which should raise a ValueError
try:
    car.speed = -10
except ValueError as e:
    print(e)  # Output: The cannot goes backward...!

# Try to set the speed to a very high value, which should raise a ValueError
try:
    car.speed = 250
except ValueError as e:
    print(e)  # Output: The speed cannot be too high, the engine is going to break.

# Set the speed of the car to 70 km/h
car.speed = 70

# Check the current speed of the car after setting it manually
print(car.speed)  # Output: 70
