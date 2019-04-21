from enum import Enum
"""
By default, enumerations allow multiple names as aliases 
for the same value. When this behavior isn’t desired, 
the following decorator can be used to ensure each value 
is used only once in the enumeration:
@enum.unique
A class decorator specifically for enumerations. It searches an enumeration’s 
__members__ gathering any aliases it finds; if any are found ValueError 
is raised with the details:
"""
from enum import Enum, unique

# @unique Class decorator for enumerations ensuring unique member values.


@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3
