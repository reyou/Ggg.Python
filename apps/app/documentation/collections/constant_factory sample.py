import collections

"""The function int() which always returns zero is just a special 
case of constant functions. A faster and more flexible way to 
create constant functions is to use a lambda function which can 
supply any constant value (not just zero):"""


def constant_factory(value):
    return lambda: value


"""The default factory is called without arguments to produce 
a new value when a key is not present, in __getitem__ only. 
A defaultdict compares equal to a dict with the same items. 
All remaining arguments are treated the same as if they were 
passed to the dict constructor, including keyword arguments."""
d = collections.defaultdict(constant_factory('<missing>'))
"""D.update([E, ]**F) -> None. Update D from dict/iterable 
E and F. If E is present and has a .keys() method, then does: 
for k in E: D[k] = E[k] If E is present and lacks a .keys() 
    method, then does: for k, v in E: D[k] = v In either 
    case, this is followed by: for k in F: D[k] = F[k]"""
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d

print(d)

# Setting the default_factory to set makes the defaultdict
# useful for building a dictionary of sets:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
"""set() -> new empty set object set(iterable) -> new set object
Build an unordered collection of unique elements."""
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)

res = sorted(d.items())
print(res)
