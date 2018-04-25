from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Enumeration members are hashable, so they can be used in dictionaries and sets:


apples = {}
apples[Color.RED] = 'red delicious'
apples[Color.GREEN] = 'granny smith'
apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'}
print(apples)
# Sometimes it’s useful to access members in enumerations programmatically
# (i.e. situations where Color.RED won’t do because the exact color is not
# known at program-writing time). Enum allows such access:

print(Color(1))

print(Color(3))

# If you want to access enum members by name, use item access:

print(Color['RED'])

print(Color['GREEN'])
# If you have an enum member and need its name or value:


member = Color.RED
print(member.name)
print(member.value)
