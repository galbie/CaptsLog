import pytest


def square(x):
    return x * x


def test_square():
    """Unit test for dummy function.
    """
    test_cases = [1, 2, 3, 4, 5]
    for number in test_cases:
        assert number ** 2 == square(number)
