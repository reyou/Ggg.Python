from collections import defaultdict
"""Using list as the default_factory, it is easy to group 
a sequence of key-value pairs into a dictionary of lists:"""
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

res = sorted(d.items())
print(res)
"""When each key is encountered for the first time, it is not 
already in the mapping; so an entry is automatically created using 
the default_factory function which returns an empty list. The 
list.append() operation then attaches the value to the new list. 
When keys are encountered again, the look-up proceeds normally 
(returning the list for that key) and the list.append() operation 
adds another value to the list. This technique is simpler and faster 
than an equivalent technique using dict.setdefault():"""
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

res = sorted(d.items())
print(res)

"""Setting the default_factory to int makes the defaultdict useful 
for counting (like a bag or multiset in other languages):"""
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

# D.items() -> a set-like object providing a view on D's items
res = sorted(d.items())
print(res)
