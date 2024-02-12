# This code is to create a class shirt, a manager class and store it on sqlite database
# still working in process 
# need to review sqlite operations
# split the code into a package to be organize and easy to perform maintenance


import sqlite3
from typing import List


class Shirt:
    """
    A simple class that models a t-shirt.

    Attributes:
    ----------
    color : str
        The color of the shirt.
    size : str
        The size of the shirt.
    style : str
        The style of the shirt.
    price: float
        The price of the the shirt

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
        return f"{__class__.__qualname__}(color='{self.color}', size='{self.size}', \
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


class ShirtManager:
    """
    A class for managing several Shirt objects using SQLite.
    """

    def __init__(self, db_name: str = 'shirts.db'):
        """
        Initialize the ShirtManager with the name of the SQLite database to use.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def __del__(self):
        """
        Clean up the ShirtManager by closing the database connection.
        """
        self.conn.close()

    def create_table(self

