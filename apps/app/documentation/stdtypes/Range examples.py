print(list(range(10)))

print(list(range(1, 11)))

print(list(range(0, 30, 5)))

print(list(range(0, 10, 3)))

print(list(range(0, -10, -1)))

print(list(range(0)))

print(list(range(1, 0)))

print(list(range(10, 0)))

print("""Range objects implement the collections.abc.Sequence ABC, 
and provide features such as containment tests, element index lookup, 
slicing and support for negative indices (see Sequence Types — 
list, tuple, range):""")

r = range(0, 20, 2)
print(r)

print(11 in r)

print(10 in r)

print(r.index(10))

print(r[5])

print(r[:5])

print(r[-1])
