import collections
"""A Counter is a dict subclass for counting hashable objects. It 
is an unordered collection where elements are stored as dictionary 
keys and their counts are stored as dictionary values. Counts are 
allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.
Elements are counted from an iterable or initialized from another 
mapping (or counter):"""
# a new, empty counter
c = collections.Counter()
# a new counter from an iterable
c = collections.Counter('gallahad')
# a new counter from a mapping
c = collections.Counter({'red': 4, 'blue': 2})
# a new counter from keyword args
c = collections.Counter(cats=4, dogs=8)
"""Counter objects have a dictionary interface except that they return 
a zero count for missing items instead of raising a KeyError:"""
c = collections.Counter(['eggs', 'ham'])
# count of a missing element is zero
print(c['bacon'])
# count of a missing element is zero
print(c['ham'])
# Setting a count to zero does not remove an element
# from a counter. Use del to remove it entirely:
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry
