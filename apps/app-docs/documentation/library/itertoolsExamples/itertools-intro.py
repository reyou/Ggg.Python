# https://docs.python.org/3.6/library/itertools.html
"""This module implements a number of iterator building blocks inspired by constructs
from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
The module standardizes a core set of fast, memory efficient tools that are useful
by themselves or in combination. Together, they form an “iterator algebra” making it
possible to construct specialized tools succinctly and efficiently in pure Python."""
import itertools

items = {1, 2, 3}
char = "a"
"""Cartesian product of input iterables.
Roughly equivalent to nested for-loops in a generator expression. 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
The nested loops cycle like an odometer with the rightmost element 
advancing on every iteration. This pattern creates a lexicographic ordering so that 
if the input’s iterables are sorted, the product tuples are emitted in sorted order.
To compute the product of an iterable with itself, specify the number of 
repetitions with the optional repeat keyword argument. For example, product(A, repeat=4) 
means the same as product(A, A, A, A)."""
qqq = itertools.product(items, char)
www = list(qqq)
print(www)
# ==============================================================================
char2 = "b"
qqq = itertools.product(items, char, char2)
www = list(qqq)
print(www)
# ==============================================================================
char2 = "b"
items2 = {'x', 'y', 'z'}
qqq = itertools.product(items, char, char2, items2)
www = list(qqq)
print(www)
# ==============================================================================
