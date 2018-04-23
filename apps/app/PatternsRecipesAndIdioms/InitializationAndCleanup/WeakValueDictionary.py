# https://docs.python.org/3.6/library/weakref.html
from weakref import WeakValueDictionary

"""Mapping class that references values weakly. 
Entries in the dictionary will be discarded when no strong reference 
to the value exists any more. Note Caution: Because a WeakValueDictionary is built on top of a 
Python dictionary, it must not change size when iterating over it. 
This can be difficult to ensure for a WeakValueDictionary because actions performed by 
the program during iteration may cause items in the dictionary to vanish “by magic” 
(as a side effect of garbage collection)."""


class Counter:
    _instances = WeakValueDictionary()

    @property
    def Count(self):
        return len(self._instances)

    def __init__(self, name):
        self.name = name
        self._instances[id(self)] = self
        print(name, 'created')

    def __del__(self):
        print(self.name, 'deleted')
        if self.Count == 0:
            print('Last Counter object deleted')
        else:
            print(self.Count, 'Counter objects remaining')


x = Counter("First")
y = Counter("Second")
