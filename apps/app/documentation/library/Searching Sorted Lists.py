"""
This module provides support for maintaining a list in sorted order without 
having to sort the list after each insertion. For long lists of items with 
expensive comparison operations, this can be an improvement over the more 
common approach. The module is called bisect because it uses a basic 
bisection algorithm to do its work. The source code may be most useful 
as a working example of the algorithm (the boundary conditions are already 
right!).
"""
import bisect


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    # Return the index where to insert item x in list a, assuming a is sorted.
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    # Inappropriate argument value (of correct type).
    # https://docs.python.org/2/library/exceptions.html
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    # Return the index where to insert item x in list a, assuming a is sorted.
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    # Return the index where to insert item x in list a, assuming a is sorted.
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    # Return the index where to insert item x in list a, assuming a is sorted.
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    # Return the index where to insert item x in list a, assuming a is sorted.
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
