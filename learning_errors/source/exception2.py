# exception2.py
'''
raise review with test unit - pytest
'''
from typing import Union


def square_root(x: Union[int, float]) -> Union[int, float]:
    """
    Calculate the square root of a number.

    Parameters:
    - x (Union[int, float]): The number whose square root is to be calculated.

    Returns:
    - Union[int, float]: The square root of the input number.

    Raises:
    - ValueError: If the input is negative.
    """
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return x ** 0.5
