a_list = [1, "4", 9, "a", 0, 4]

"""Return whether an object is an instance of a class or of a subclass thereof.
A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to 
check against. This is equivalent to isinstance(x, A) or isinstance(x, B) 
or ... etc."""
squared_ints = [e ** 2 for e in a_list if isinstance(e, int)]
print(squared_ints)
"""Lambda expressions (sometimes called lambda forms) are used to create anonymous functions. 
The expression lambda arguments: expression yields a function object. """
filtered = filter(lambda e: isinstance(e, int), a_list)
squared_ints2 = map(lambda e: e ** 2, filtered)
print(squared_ints)
