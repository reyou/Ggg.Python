# Metaprogramming/SimpleMeta2.py
# Combining the steps for metaclass creation in Python 2.x
"""The compiler won’t accept the super() call because it says __metaclass__
hasn’t been defined, forcing
us to use the specific call to type.__init__()."""
class Simple2(object):
    class __metaclass__(type):
        def __init__(cls, name, bases, nmspc):
            # This won't work:
            # super(__metaclass__, cls).__init__(name, bases, nmspc)
            # Less-flexible specific call:
            type.__init__(cls, name, bases, nmspc)
            cls.uses_metaclass = lambda self: "Yes!"


class Simple3(Simple2): pass


simple = Simple3()
print(simple.uses_metaclass())
