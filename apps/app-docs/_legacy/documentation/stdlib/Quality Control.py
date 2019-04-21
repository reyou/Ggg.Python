"""The doctest module provides a tool for scanning a module
and validating tests embedded in a program’s docstrings.
Test construction is as simple as cutting-and-pasting
a typical call along with its results into the docstring.
This improves the documentation by providing the user
with an example and it allows the doctest module to make
sure the code remains true to the documentation:"""


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

# automatically validate the embedded tests
doctest.testmod()
