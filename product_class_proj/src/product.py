# OOP/product.py 

class Product:
    """
    A class the models a product with three attributes: name, description, price
    
    Attributes:
        name (str): Product name.
        description (str): Description of the product.
        price (float): The price of the product.
    
    Examples:
        >>> p1 = Product('PS5', 'Console Gamer', 4500)
        >>> p1.name
        'PS5'
        >>> p1.description
        'Console Gamer'
        >>> p1.price
        4500
    """
    def __init__(self, name: str, description: str, price: float) -> None:
        """
        The constructor for the Product class
        Parameters:
            name (str): The name of the product object.
            description (str): The description of the product object
            price (float): The price of the product.
        """            
        self.name = name
        self.description = description
        self.price = price
        
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the object.
        Returns:
            str: a human-readable string representation of the object
        """
        return f"Product: name={self.name}, description={self.description}, price={self.price}"
    
    def __repr__(self) -> str:
        """
        Method that returns a string representation of the object that can be used to recreate it.
        Returns:
            str: a string representation of the instance.
        """        
        return f"{__class__.__qualname__}('{self.name}', '{self.description}', {self.price})"    


if __name__ == "__main__":
    pass