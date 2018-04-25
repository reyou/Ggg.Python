import collections
"""Elements are subtracted from an iterable or from another 
mapping (or counter). Like dict.update() but subtracts counts 
instead of replacing them. Both inputs and outputs may be zero 
or negative."""
"""Counter: Dict subclass for counting hashable items. Sometimes 
called a bag or multiset. Elements are stored as dictionary keys 
and their counts are stored as dictionary values."""
c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
