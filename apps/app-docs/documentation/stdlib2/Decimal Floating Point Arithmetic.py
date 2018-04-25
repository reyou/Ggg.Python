# https://docs.python.org/3/tutorial/stdlib2.html#decimal-floating-point-arithmetic
"""For example, calculating a 5% tax on a 70 cent phone charge gives different
results in decimal floating point and binary floating point. The difference
becomes significant if the results are rounded to the nearest cent:"""
from decimal import *

r1 = round(Decimal('0.70') * Decimal('1.05'), 2)
print(r1)
r2 = round(.70 * 1.05, 2)
print(r2)
