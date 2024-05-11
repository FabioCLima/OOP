# exception4.py
'''
Creating custom errors
    >>>Inheritance
    >>>Built in Errors
'''


class MyCustonError(TypeError):
    """Exception raised for errors related to invalid input in my_function.

    Attributes:
        message (str): Explanation of the error.
        code (int): Error code associated with the error.
    """

    def __init__(self, message: str, code: int) -> None:
        """Initialize MyCustomError with the given message and error code.

        Args:
            message (str): Explanation of the error.
            code (int): Error code associated with the error.
        """
        super().__init__(f"Error code {code}: {message}")
        self.code = code


def my_function(x) -> None:
    """Converts input to a number and prints it.

    Args:
        x (str): The input to be converted to a number.

    Raises:
        MyCustomError: If the input cannot be converted to a number.
    """
    try:
        # Try to convert to a number first
        number = float(x)
    except ValueError:
        # if conversion to float fails, try converting to int
        try:
            number = int(x)
        except ValueError:
            # if both conversions fail, raise an error
            raise MyCustonError("Input must be a valid number not a string", 5)

    print(f"The provide number was {number}")


if __name__ == "__main__":
    x = input('Provide a number: ')
    my_function(x)
