from enum import Enum
"""
However, two enum members are allowed to have the same value. 
Given two members A and B with the same value (and A defined first), 
B is an alias to A. By-value lookup of the value of A and B will 
return A. By-name lookup of B will also return A:
"""


class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2


print("\n", "Shape.SQUARE", "(" + str(type(Shape.SQUARE)) + ") =>")
print(Shape.SQUARE)
print("\n")

print("\n", "Shape.ALIAS_FOR_SQUARE",
      "(" + str(type(Shape.ALIAS_FOR_SQUARE)) + ") =>")
print(Shape.ALIAS_FOR_SQUARE)
print("\n")

print("\n", "Shape(2)", "(" + str(type(Shape(2))) + ") =>")
print(Shape(2))
print("\n")
