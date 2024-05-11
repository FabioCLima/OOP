# __main__.py
'''
Main module to test all the module class created in
this project.
'''

from car.car import Car
from eletric_car.eletricCar import Battery, ElectricCar


def main():
    # Creating a Car object
    nivus = Car('Wolkswagen', 'suv nivus', 2024)
    nivus.gas_tank = True

    # Display the descriptive name of the car
    print(nivus.get_descriptive_name())

    # Check the current odometer reading
    print(f"Odometer reading from my new car - {nivus} is \
{nivus.odometer_reading} km")

    # Set the odometer reading
    try:
        nivus.odometer_reading = 100
    except ValueError as error:
        print(error)

    # Increment the odometer reading
    try:
        nivus.increment_odometer(50)
    except ValueError as error:
        print(error)


if __name__ == "__main__":

    main()
