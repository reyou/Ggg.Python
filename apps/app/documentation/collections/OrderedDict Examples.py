import collections
from collections import OrderedDict
# regular unsorted dictionary
dictionaryInstance = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
res = OrderedDict(sorted(dictionaryInstance.items(), key=lambda t: t[0]))
print("\n res")
print(res)

# dictionary sorted by value
res = OrderedDict(sorted(dictionaryInstance.items(), key=lambda t: t[1]))
print("\n res")
print(res)

# dictionary sorted by length of the key string
res = OrderedDict(sorted(dictionaryInstance.items(), key=lambda t: len(t[0])))
print("\n res")
print(res)
"""
The new sorted dictionaries maintain their sort order when entries are deleted. 
But when new keys are added, the keys are appended to the end and the sort 
is not maintained.
It is also straight-forward to create an ordered dictionary variant that remembers 
the order the keys were last inserted. If a new entry overwrites an existing 
entry, the original insertion position is changed and moved to the end:
"""


class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        # Set self[key] to value.
        OrderedDict.__setitem__(self, key, value)


lastUpdatedOrderedDict = LastUpdatedOrderedDict(res)
res = lastUpdatedOrderedDict
print("\n lastUpdatedOrderedDict", "(" + str(type(res)) + ") =>")
print(lastUpdatedOrderedDict)

"""
An ordered dictionary can be combined with the Counter class so that the 
counter remembers the order elements are first encountered:
"""


class OrderedCounter(collections.Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    # https://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python
    def __repr__(self):
        print("\ncalling __repr__")
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        print("\ncalling __reduce__")
        return self.__class__, (OrderedDict(self),)


# a new, empty counter
counter = collections.Counter()
orderedCounter = OrderedCounter(lastUpdatedOrderedDict)
res = orderedCounter
print("\n orderedCounter232", "(" + str(type(res)) + ") =>")
print(str(orderedCounter))
