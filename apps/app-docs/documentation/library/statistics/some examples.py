from statistics import mean, median
from fractions import Fraction as F
from decimal import Decimal as D

# Return the sample arithmetic mean of data.
print("mean", mean([1, 2, 3, 4, 4]))
print("median", median([1, 2, 3, 4, 4]))
print("eee", mean([-1.0, 2.5, 3.25, 5.75]))
print("www", mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print("fff", mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")]))
