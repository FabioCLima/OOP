class Shirt:
    """
    The `Shirt` class represents a basic shirt with color, size, style,
    and price information. It allows modifying the price and calculating the
    discounted price.

    Attributes:
        color (str): The color of the shirt.
        size (str): The size of the shirt.
        style (str): The style of the shirt.
        price (float): The original price of the shirt.

    Methods:
        __init__(self, color: str, size: str, style: str, price:
                float) -> None:
            Initializes a new instance of the `Shirt` class with the provided
            attributes.

        change_price(self, new_price: float) -> None:
            Changes the price of the shirt to the specified `new_price`.

        discount(self, discount: float) -> float:
            Calculates the discounted price of the shirt based on the given
            discount percentage.

        __repr__(self) -> str:
            Returns a string representation of the `Shirt` object that can be
            used to recreate the object.

        __str__(self) -> str:
            Returns a string representation of the `Shirt` object that is
            user-friendly.

    Examples:
        # Creating a new shirt instance
        >>> shirt1 = Shirt("Blue", "Medium", "Casual", 25.99)

        # Changing the price of the shirt
        >>> shirt1.change_price(19.99)

        # Printing the shirt object
        >>> print(shirt1)
        A Blue shirt of size Medium with style 'Casual' is priced at $19.99.
    """

    def __init__(self, color: str, size: str, style: str,
                 price: float) -> None:
        """
        Initializes a new instance of the `Shirt` class.

        Args:
            color (str): The color of the shirt.
            size (str): The size of the shirt.
            style (str): The style of the shirt.
            price (float): The original price of the shirt.
        """
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, new_price: float) -> None:
        """
        Changes the price of the shirt to the specified `new_price`.

        Args:
            new_price (float): The new price to be set for the shirt.
        """
        self.price = new_price

    def discount(self, discount: float) -> float:
        """
        Calculates the discounted price of the shirt based on the given
        discount percentage.

        Args:
            discount (float): The discount percentage in decimal form
            (e.g., 0.1 for 10% discount).

        Returns:
            float: The discounted price of the shirt.
        """
        return self.price * (1 - discount)

    def __repr__(self) -> str:
        """
        Returns a string representation of the `Shirt` object that can be used
        to recreate the object.

        Returns:
            str: A string representation of the `Shirt` object.
        """
        return (
            f"Shirt(color='{self.color}', size='{self.size}',"
            f"style='{self.style}', price={self.price})"
        )

    def __str__(self) -> str:
        """
        Returns a string representation of the `Shirt` object that is
        user-friendly.

        Returns:
            str: A user-friendly string representation of the `Shirt` object.
        """
        return (
            f"A {self.color} shirt of size {self.size} with style"
            f" '{self.style}' is priced at ${self.price:.2f}."
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
