from typing import Union

class Mass:
    
    def __init__(self, kg: Union[int, float]) -> None:
        self.kg = kg
        
    def __str__(self) -> str:
        return f"Mass(kilogram = {self.kg})"
    
    def __add__(self, other: float):
        if isinstance(other, Mass):
            return Mass(self.kg + other.kg)
        else: 
            raise ValueError("unsupported operand type(s) for +: 'Mass' and + str(type()other)")
    
    @property    
    def grams(self) -> Union[int, float]:
        """
        Getter method that returns the grams from the kilograms as input.
        Returns:
            _type_: _description_
        """        
        return self.kg * 1000
    
    @grams.setter
    def grams(self, grams: Union[int, float]):
        """
        Setter method that returns the kilograms from the grams as input.

        Args:
            grams (Union[int, float]): _description_
        """        
        self.kg = grams / 1000
        
    @grams.deleter
    def grams(self):
        print("Resetting mass !")
        self.kg = 0
