"""
The fractions module provides support for rational number arithmetic.
A Fraction instance can be constructed from a pair of integers, from 
another rational number, or from a string.
"""
from fractions import Fraction
print("Fraction(16, -10)", Fraction(16, -10))
print("Fraction(123)", Fraction(123))
print("Fraction()", Fraction())
print(" Fraction('3/7')", Fraction('3/7'))
print("Fraction(' -3/7 ')", Fraction(' -3/7 '))
print(" Fraction('1.414213 \t\n')", Fraction('1.414213 \t\n'))
print("Fraction('-.125')", Fraction('-.125'))
print("Fraction('7e-6')", Fraction('7e-6'))
print("Fraction(2.25)", Fraction(2.25))
print("Fraction(1.1)", Fraction(1.1))


from decimal import Decimal
print("Fraction(Decimal('1.1'))", Fraction(Decimal('1.1')))
