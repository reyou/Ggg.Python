"""
Ordered dictionaries are just like regular dictionaries but they remember the 
order that items were inserted. When iterating over an ordered dictionary, 
the items are returned in the order their keys were first added.
"""
from collections import OrderedDict
"""
OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S. If not 
specified, the value defaults to None.
"""
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
res = ''.join(d.keys())
print("\n res")
print(res)

d.move_to_end('b', last=False)
res = ''.join(d.keys())
print("\n res")
print(res)
