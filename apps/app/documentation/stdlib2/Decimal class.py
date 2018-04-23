# https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic
"""Exact representation enables the Decimal class to perform modulo
calculations and equality tests that are unsuitable for binary
floating point:"""
from decimal import *

Decimal('1.00') % Decimal('.10')

print("result of 1.00 % 0.10:")
print(1.00 % 0.10)

r1 = sum([Decimal('0.1')] * 10) == Decimal('1.0')
print("r1")
print(r1)
r2 = sum([0.1] * 10) == 1.0
print("r2")
print(r2)

print("\nThe decimal module provides arithmetic with as much precision as needed:")
print("getcontext().prec = 36")
getcontext().prec = 36
print("Decimal(1) / Decimal(7)")
print(Decimal(1) / Decimal(7))
