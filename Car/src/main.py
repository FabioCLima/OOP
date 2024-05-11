# main.py
from car import Car, ElectricCar


def main():

    my_used_car = Car('subaru', 'outback', 2019)
    nivus = Car('Nivus', 'suv', 2022)
    print(my_used_car.get_descriptive_name())

    my_used_car.update_odometer(23_500)
    my_used_car.read_odometer()

    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()

    nivus.get_descriptive_name()
    print(nivus.get_descriptive_name())
    nivus.update_odometer(100)
    nivus.read_odometer()
    nivus.increment_odometer(-1000)

    # Modify an attribute value directly
    my_new_car = Car('Volvo', 'suv', 2024)
    print(f"\n{my_new_car}")
    print(f"{my_new_car.get_descriptive_name()}")
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    my_new_car.update_odometer(100)
    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())

    # The last new_car
    nivus_2024 = Car('Wolksvagen', 'suv', 2024)
    print(f"\n{nivus_2024}")
    nivus_2024.fill_gas_tank()
    print(my_leaf)
    my_leaf = ElectricCar('nissan', 'leaf', 2024)
    print(my_leaf.get_descriptive_name())
    my_leaf.battery.describe_battery()
    my_leaf.battery.get_range()


if __name__ == "__main__":
    main()
