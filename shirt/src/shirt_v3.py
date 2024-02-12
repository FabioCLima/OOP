# Udacity exercises
# shirt class version 1
from typing import List

class Shirt:
    
    num_instances = 0
    """
    A simple class that models a t-shirt.

    Attributes of instance:
    ----------------------
    color : str
        The color of the shirt.
    size : str
        The size of the shirt.
    style : str
        The style of the shirt.
    price: float
        The price of the the shirt
        
    Attributes of class:
    --------------------
    num_instances : holds the information about the number os object create of Class
    
    Example:
        >>> new_shirt = Shirt("Blue", "XL", "Polo", 24.99)
        >>> new_shirt.color
        'Blue'
        >>> new_shirt.size
        'XL'
        >>> new_shirt.style
        'Polo'
        >>> new_shirt.price
        24.99
    """

    def __init__(self, 
                 shirt_color: str, 
                 shirt_size: str, 
                 shirt_style: str, 
                 shirt_price: float) -> None:

        """
            Initialize the Shirt class with its attributes.

        Args:
            shirt_color: A string representing the color of the shirt.
            shirt_size: A string representing the size of the shirt.
            shirt_style: A string representing the style of the shirt.
            shirt_price: A float representing the price of the shirt.
        """

        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
        
        # 
        Shirt.num_instances += 1

    def __str__(self) -> str:
        """
        Returns a string representation of the shirt.
        """
        return f"Shirt(color='{self.color}', size='{self.size}',\
style='{self.style}', price={self.price})"

    def __repr__(self) -> str:
        """
        Returns a string representation of the shirt that can be used to
        recreate the object.
        """
        return f"{__class__.__name__}(color='{self.color}', size='{self.size}', \
    style='{self.style}', price={self.price})"

    def change_price(self, new_price: float):
        """
        Changes the price of the product.

        Args:
        new_price (float): The new price of the product.

        Returns:
        None.

        Example:
            >>> new_shirt = Shirt("Blue", "XL", "Polo", 24.99)
            >>> new_shirt.price
            24.99
            >>> new_shirt.change_price(30.05)
            >>> new_shirt.price
            30.05
    """
        self.price = new_price

    def discount(self, discount: float) -> float:
        """
        The method discount takes in a single parameter discount which is a 
        float representing the percentage discount to be applied to the price
        of the instance of the class that this method is called on. 

        Args:
            discount (float): the percentage discount to be applied.

        Returns:
            float: he discounted price of the instance of the class 
            that this method is called on
        """        
        return self.price * (1-discount)
    
    @classmethod
    def get_num_instances(cls):
        return cls.num_instances


if __name__ == "__main__":

    # In this refactored code:
    # - I changed the `Shirt` class to have `__init__`, `change_price`, and `discount` methods.
    # - I added the `__dict__` attribute to Example 1 to display the shirt object's attributes.
    # - I put the code examples inside the `__main__` conditional.
    # - I used the `extend` method to add multiple t-shirts to `tshirt_collection`.
    # - I simplified the `for` loop in Example 4 by iterating through the `tshirt_collection` list directly.
    # Example 1: Creating a new shirt object with attributes and printing it
    # out as string.
    
    import json
    
    new_shirt = Shirt("Blue", "XL", "Polo", 24.99)
    print(new_shirt.__dict__)

    # Example 2: Changing the price of an existing Shirt object and then 
    # printing out the updated price.
    new_shirt2 = Shirt("Green", "L", "Polo", 24.99)
    new_shirt2.change_price(19.99)
    print(new_shirt2.price)

    # Example 3: Applying a discount to an existing Shirt object and then 
    # printing out the discounted price.
    new_shirt3 = Shirt("Yellow", "M", "Button Up", 34.99)
    discounted_price = new_shirt3.discount(0.2)
    print(discounted_price)
    
    # Get the number of instance of shirt create
    print(f"The number of shirts created so far is:{Shirt.get_num_instances()}")
    # Create a collection of tshirt 
    # Manager more than on object or instance from the same class
    shirt_bd = [vars(new_shirt), new_shirt2.__dict__, vars(new_shirt3)]
    tshirt_collection= []
    tshirt_collection.extend((new_shirt, new_shirt2, new_shirt3))
    for item in tshirt_collection:
        print(item.color)
    
    file_out = "/home/fabio/Desktop/projects/classes/shirt/shirt_colection.json"    
    with open(file_out, 'w') as file:
        json.dump(shirt_bd, file, ensure_ascii=False, indent=2)