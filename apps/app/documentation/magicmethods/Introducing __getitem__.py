"""Implementing __getitem__ in a class allows its instances 
to use the [] (indexer) operators."""
"""The __getitem__ magic method is usually used for list indexing, 
dictionary lookups, or accessing ranges of values. Considering how 
versatile (çok yönlü) it is, it's probably one of Python's most 
underutilized magic methods."""


class Test(object):
    def __getitem__(self, items):
        print('%-15s  %s' % (type(items), items))


t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]
