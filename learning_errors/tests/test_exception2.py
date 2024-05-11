# test_exception2.py

import pytest
import source.exception2 as my_functions


def test_square_root_negative_number():
    """
    Test case to verify that square_root function raises ValueError for
    negative input. This we expected to fail
    """
    x = -4
    with pytest.raises(ValueError):
        my_functions.square_root(x)


def test_square_root_positive_number():
    """
    Test case to verify that square_root function returns correct square root
    for positive input.
    """
    x = 4
    expected_result = 2
    result = my_functions.square_root(x)
    assert result == expected_result, "Check the square_root function"
