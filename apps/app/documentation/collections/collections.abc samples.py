"""
Several of the ABCs are also useful as mixins that make it easier 
to develop classes supporting container APIs. For example, to write 
a class supporting the full Set API, it is only necessary to supply 
the three underlying abstract methods: __contains__(), __iter__(), 
and __len__(). The ABC supplies the remaining methods such as __and__() 
and isdisjoint():
"""
import collections


class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''

    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)


s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically
res = s1
print("\n", "s1", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
res = s2
print("\n", "s2", "(" + str(type(res)) + ") =>")
print(res)
print("\n")
