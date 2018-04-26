# auto: Instances are replaced with an appropriate value in Enum class suites.
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


res = list(Color)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")

# The values are chosen by _generate_next_value_(), which can be overridden:
"""
Note The goal of the default _generate_next_value_() methods is to provide 
the next int in sequence with the last int provided, but the way it does 
this is an implementation detail and may change.
"""


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


res = list(Ordinal)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
