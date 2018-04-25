"""Implementing __getattr__ overrides Python's default 
mechanism for member access."""


class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456


t = Test()
print('object variables: %r' % t.__dict__.keys())
print("\n t.a")
print(t.a)
print("\n t.b")
print(t.b)
print("\n t.c")
print(t.c)
"""Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y. 
When a default argument is given, it is returned when the attribute 
doesn't exist; without it, an exception is raised in that case."""
print("\n getattr")
print(getattr(t, 'd'))
"""Return whether the object has an attribute with the given name.
This is done by calling getattr(obj, name) and catching AttributeError."""
print("\n hasattr")
print(hasattr(t, 'x'))
"""As you can see from the example above, the __getattr__ magic 
method only gets invoked for attributes that are not in the __dict__ 
magic attribute. Implementing __getattr__ causes the hasattr built-in 
function to always return True, unless an exception is raised from 
within __getattr__."""
