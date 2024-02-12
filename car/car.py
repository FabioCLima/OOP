# python projects - book

# The Car Class
from datetime import date

class Car:
    """
    A simple attempt to represent a car.
    """
    
    def __init__(self, make: str, model: str, year: date) -> None:
        """
        Initialize attributes to describe a car.

        Args:
            make (str): The car make eg. Honda, Ford
            model (str): The car's model eg. sedan
            year (datetime): The year of car's fabrication.
        """
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading: float = 0
        self.__speed: int = 0
        
    def __str__(self) -> str:
        """
        A string representation of the car object.
        Returns:
            str: A representation of the Car class.
        """        
        
        return f"Car({self.make}, {self.model}, {self.year})"
    
    def get_descriptive_name(self) -> str:
        """
        Return a neatly formatted descriptive name.
        """
        long_name = f"{self.year} {self.make } {self.model}"      
        return long_name.title()
    
    def read_odometer(self) ->None:
        """
        Print a statement showing the car's mileage
        """
        print(f"This car has {self.odometer_reading} miles on it.")     
        
    def update_odometer(self, mileage: float) -> float:
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.

        Args:
            mileage (float): The new mileage car value.

        Returns:
            int: The odometer's car updated with new given value.
        """ 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer. ")
            
    def increment_odometer(self, miles: float) -> float:
        """
        Add the given amount to the odometer reading

        Args:
            miles (int): Miles will be add to the odometer.

        Returns:
            int: The amount of Miles which will be add to the odometer reading.
        """ 
        if miles >=0:                 
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer.")
    
    def accelerate(self, speed: int):
        self.__speed += speed

    def brake(self, speed: int):
        self.__speed = max(0, self.__speed - speed)

    # def get_speed(self) -> int:
    #     return self.__speed
    
    @property
    def speed(self) -> int:
        return self.__speed
    
    @speed.setter
    def speed(self, speed: int):
        if speed < 0:
            raise ValueError('The cannot goes backward...!')
        elif speed > 200:
            raise ValueError('The speed cannot be too high, the engine is going to break.')
        else:
            self.__speed = speed
            
    
if __name__ == "__main__":
    
    car = Car('Honda', 'Civic', date(2020, 1, 1).year)
    print(car)
    print(f"The of car's making: {car.year}")
    car.accelerate(100)
    print()
    print(f"The speed of the car is: {car.speed}")  
    car.brake(67)
    print(f"The current car speed: {car.speed}")
    # car.speed = -10
    # print(f"{car.speed}")
    car.speed = 210
    print(f"The current car speed: {car.speed}")
    