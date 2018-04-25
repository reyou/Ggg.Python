"""
Enumerations are created using the class syntax, which 
makes them easy to read and write. An alternative creation 
method is described in Functional API. To define an enumeration, 
subclass Enum as follows:
"""
from enum import Enum

"""
Member values can be anything: int, str, etc.. If the exact 
value is unimportant you may use auto instances and an appropriate 
value will be chosen for you. Care must be taken if you mix auto 
with other values.
"""
"""
Note Even though we use the class syntax to create Enums, 
Enums are not normal Python classes. See How are Enums different? 
for more details.
"""


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(repr(Color.RED))
# The type of an enumeration member is the enumeration it belongs to:
type(Color.RED)

isinstance(Color.GREEN, Color)
# Enum members also have a property that contains just their item name:

print(Color.RED.name)
