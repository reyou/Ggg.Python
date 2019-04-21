# https://docs.python.org/3/library/functions.html#zip
print("\nx = [1, 2, 3]:")
x = [1, 2, 3]
print("\ny = [4, 5, 6]:")
y = [4, 5, 6]
"""Return a zip object whose .__next__() method returns a tuple where the 
i-th element comes from the i-th iterable argument. The .__next__() method 
continues until the shortest iterable in the argument sequence is exhausted 
and then it raises StopIteration."""
zipped = zip(x, y)
print("\nzipped:")
print(zipped)
print("\nlist(zipped):")
"""list() -> new empty list list(iterable) -> new list initialized from 
iterable's items # (copied from class doc)"""
print(list(zipped))

print("\nx2, y2 = zip(*zip(x, y)):")
x2, y2 = zip(*zip(x, y))
print("\nx2:")
print(x2)
print("\ny2:")
print(y2)
print("\nx == list(x2) and y == list(y2):")
print(x == list(x2) and y == list(y2))
