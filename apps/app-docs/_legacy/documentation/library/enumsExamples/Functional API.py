# The Enum class is callable, providing the following functional API:
from enum import Enum
Animal = Enum('Animal', 'ANT BEE CAT DOG')


print("\n", "Animal", "(" + str(type(Animal)) + ") =>")
print(Animal)
print("\n")
print("\n", "Animal.ANT", "(" + str(type(Animal.ANT)) + ") =>")
print(Animal.ANT)
print("\n")

print("\n", "Animal.ANT.value", "(" + str(type(Animal.ANT.value)) + ") =>")
print(Animal.ANT.value)
print("\n")
res = list(Animal)
print("\n", "res", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
